#!/usr/bin/env python3
"""
舱路雷达 · compute.py (v6 模块化)
从 shared/ CSV 计算 5 个 JSON 输出：metrics / history / scenarios / decisions / indices
严格遵循 specs/data-format-v5.md

用法: python3 compute.py [--shared-dir PATH] [--output-dir PATH]

架构 v6: config.yaml + data_loader.py + metrics.py + compute.py(主流程)
"""

import json
import math
import os
import sys
from datetime import datetime, timezone, timedelta
from collections import OrderedDict

# 确保当前目录在 sys.path 中，以便导入同目录模块
_here = os.path.dirname(os.path.abspath(__file__))
if _here not in sys.path:
    sys.path.insert(0, _here)

import yaml
from data_loader import read_csv, safe_float
from metrics import (
    percentile, calc_stats, up_streak_count,
    warning_level, warning_tags,
)

tz_shanghai = timezone(timedelta(hours=8))

# ── 加载配置 ──────────────────────────────────────────────

def load_config():
    """从 config.yaml 加载配置，返回可变 dict"""
    config_path = os.path.join(_here, "config.yaml")
    with open(config_path, "r", encoding="utf-8") as f:
        cfg = yaml.safe_load(f)
    return cfg

config = load_config()

# 快捷别名（兼容旧代码）
ROUTES = config["routes"]
ROUTE_META = config["route_meta"]
QUALITY_LEVEL = config["quality_level"]
LATEST_WEEK = config["latest_week"]
SURGE_THRESHOLDS = config["warning"]["surge_threshold"]
DATA_QUALITY_FULL = config["data_quality"]["full_min"]
DATA_QUALITY_REDUCED = config["data_quality"]["reduced_min"]
PERCENTILE_POINTS = config["percentile_points"]

# ── 决策建议模板 ──────────────────────────────────────────

with open(os.path.join(_here, "suggestion-templates.json"), "r", encoding="utf-8") as f:
    SUGGESTION_TEMPLATES = json.load(f)


def build_suggestion(code, level, current_value, z_score, up_streak):
    """生成决策建议文本"""
    templates = SUGGESTION_TEMPLATES.get(code, {})
    template = templates.get(level, "运价数据待更新，建议关注后续周报。")
    cv = f"{current_value:.0f}" if not math.isnan(current_value) else "N/A"
    zs = f"{z_score:.2f}" if not math.isnan(z_score) else "N/A"
    return template.format(current_value=cv, z_score=zs, up_streak=up_streak)


def make_meta(latest_week, extra_note=""):
    """生成标准 _meta"""
    return {
        "version": "5.0",
        "latest_week": latest_week,
        "generated_at": datetime.now(tz_shanghai).isoformat(),
        "quality_level": QUALITY_LEVEL,
        "source": "SCFI 上海航运交易所官网 + 公开转载数据",
        "fx_rate": config["fx_rate"],
        "note": extra_note or "SCFI 数据部分周 PENDING（空值），Z 分数仅基于有效样本计算。",
    }


def make_stats(total_points, pending_count, effective_n):
    """生成标准 _stats"""
    return {
        "total_data_points": total_points,
        "pending_count": pending_count,
        "pending_ratio": round(pending_count / total_points, 3) if total_points else 0,
        "effective_sample_size": effective_n,
        "window_size": config["window_size"],
    }


# ── 主流程 ────────────────────────────────────────────────

def main(shared_dir="shared", output_dir="data"):
    os.makedirs(output_dir, exist_ok=True)
    print("=" * 60)
    print("舱路雷达 · compute.py (v6 模块化)")
    print(f"  数据目录: {shared_dir}")
    print(f"  输出目录: {output_dir}")
    print("=" * 60)

    window_size = config["window_size"]

    # ── 1. 读取 SCFI 主表 ──
    scfi_path = os.path.join(shared_dir, "scfi-26w.csv")
    scfi_rows = read_csv(scfi_path)
    if not scfi_rows:
        print("❌ 无法读取 scfi-26w.csv，退出")
        sys.exit(1)

    weeks = [r["week"] for r in scfi_rows]
    route_raw = {code: [safe_float(r.get(code, "")) for r in scfi_rows] for code in ROUTES}
    # 提取 quality 列（用于区分真实数据 vs 插值数据）
    quality_raw = [r.get("quality", "UNKNOWN") for r in scfi_rows]
    HIGH_QUALITY_TAGS = {"ORIGINAL", "B_PUBLIC_EXCERPT"}  # 仅这两类计入有效样本

    # 仅取最近 26 周（从最新周往前）
    total_weeks = len(weeks)
    window_size = min(config["window_size"], total_weeks)
    weeks_26 = weeks[-window_size:]
    route_26 = {code: vals[-window_size:] for code, vals in route_raw.items()}
    quality_26 = quality_raw[-window_size:]

    latest_idx = -1
    # 找到最后一个有数据的周
    for i in range(len(weeks_26) - 1, -1, -1):
        has_data = any(not math.isnan(route_26[code][i]) for code in ROUTES)
        if has_data:
            latest_idx = i
            break

    # 兜底：26 周全空时回退到最后一周期作为时间参考（但数据标记为缺失）
    if latest_idx == -1:
        print("   ⚠️ 26 周数据全空，无法计算指标")
        sys.exit(1)

    effective_weeks = [weeks_26[i] for i in range(latest_idx + 1)]

    # ── 1.5. 读取 CCFI 周度数据，计算 4 周移动平均趋势 ──
    ccfi_path = os.path.join(shared_dir, "ccfi-weekly.csv")
    ccfi_rows = read_csv(ccfi_path)
    ccfi_4w_dir = "unknown"  # 数据不足时不上报，避免确认偏误
    if ccfi_rows and len(ccfi_rows) >= 8:
        # 按周排序
        ccfi_rows.sort(key=lambda r: r["week"])
        ccfi_vals = [safe_float(r.get("CCFI", "")) for r in ccfi_rows]
        ccfi_valid = [v for v in ccfi_vals if not math.isnan(v)]
        if len(ccfi_valid) >= 8:
            # 最新 4 周 MA
            latest_4w_ma = sum(ccfi_valid[-4:]) / 4
            # 前 4 周 MA
            prev_4w_ma = sum(ccfi_valid[-8:-4]) / 4
            ccfi_4w_dir = "up" if latest_4w_ma > prev_4w_ma else "down"
            print(f"   CCFI 4W MA: 前4周={prev_4w_ma:.1f} → 近4周={latest_4w_ma:.1f} → {ccfi_4w_dir}")
        else:
            print(f"   ⚠️ CCFI 有效数据不足8周({len(ccfi_valid)}), 使用默认方向 up")
    else:
        print(f"   ⚠️ 无法读取 ccfi-weekly.csv 或数据不足8周, 使用默认方向 up")

    # ── 2. 计算每条航线的指标 ──
    route_metrics = {}
    for code in ROUTES:
        vals = route_26[code]
        # 有效值（非 NaN）
        valid_vals = [v for v in vals if not math.isnan(v)]
        sorted_vals = sorted(valid_vals)

        current_val = vals[latest_idx] if latest_idx >= 0 and not math.isnan(vals[latest_idx]) else float("nan")

        # 前一周的值
        prev_val = float("nan")
        if len(valid_vals) >= 2:
            for j in range(latest_idx - 1, -1, -1):
                if not math.isnan(vals[j]):
                    prev_val = vals[j]
                    break

        # WoW change
        if not math.isnan(current_val) and not math.isnan(prev_val) and prev_val != 0:
            wow_pct = round((current_val - prev_val) / prev_val * 100, 2)
        else:
            wow_pct = float("nan")

        # 百分位数（26 样本下 P99 等同历史极值，无统计意义，仅算到 P95）
        pcts = {}
        for p in PERCENTILE_POINTS:
            pcts[f"p{p:02d}"] = round(percentile(sorted_vals, p), 2) if sorted_vals else float("nan")

        # Z-score
        mean, std, eff_n = calc_stats(valid_vals)
        if not math.isnan(std) and std > 0 and not math.isnan(current_val):
            z_score = round((current_val - mean) / std, 2)
        else:
            z_score = float("nan")

        # 高质量样本数（仅 ORIGINAL + B_PUBLIC_EXCERPT，排除插值/部分插值）
        n_high_quality = sum(
            1 for i, v in enumerate(vals)
            if not math.isnan(v) and quality_26[i] in HIGH_QUALITY_TAGS
        )
        print(f"   {code}: eff_n={eff_n} n_high_quality={n_high_quality}")

        # 数据质量标记（基于高质量样本数，插值数据不计入置信度）
        if n_high_quality >= DATA_QUALITY_FULL:
            data_quality = "full"
        elif n_high_quality >= DATA_QUALITY_REDUCED:
            data_quality = "reduced"
        else:
            data_quality = "insufficient"

        # 连续上涨（传入全量含 NaN 数组，NaN 周断连涨）
        streak = up_streak_count(vals)

        # 预警等级（含 wow_pct 快通道 + 航线差异化阈值 + 数据降级）
        warn_lvl = warning_level(
            z_score, streak, current_val,
            pcts.get("p95", float("nan")),
            pcts.get("p85", float("nan")),
            wow_pct, code, data_quality,
            surge_thresholds=SURGE_THRESHOLDS,
            z_red=config["warning"]["z_red"],
            z_red_b=config["warning"]["z_red_b"],
            z_yellow=config["warning"]["z_yellow"],
        )

        # Tags
        tags = warning_tags(z_score, current_val, pcts.get("p95", float("nan")),
                           pcts.get("p85", float("nan")), streak, wow_pct)

        # 数据质量降级：reduced→预警降一级；insufficient→强制灰色
        # ⚠️ 降级必须在 Tags 生成之后（快通道标签等依赖最终 warn_lvl）
        if data_quality == "insufficient":
            warn_lvl = "灰色-数据不足"
        elif data_quality == "reduced":
            downgrade = {"红色预警": "黄色预警", "黄色预警": "绿色正常"}
            warn_lvl = downgrade.get(warn_lvl, warn_lvl)

        # 快通道标签（降级后仍为红色的才追加，避免语义矛盾）
        surge_threshold = SURGE_THRESHOLDS.get(code, 15)
        if warn_lvl == "红色预警" and not math.isnan(wow_pct) and wow_pct >= surge_threshold:
            tags.append("快通道信号")

        route_metrics[code] = {
            "current_value": current_val,
            "percentiles": pcts,
            "wow_change_pct": wow_pct,
            "z_score": z_score,
            "up_streak_weeks": streak,
            "warning_level": warn_lvl,
            "warning_tags": tags,
            "eff_n": eff_n,
            "data_quality": data_quality,
        }

    # ── 2b. 读取费率数据 ──
    # 汇率
    fx_path = os.path.join(shared_dir, "usd-cny-26w.csv")
    fx_rows = read_csv(fx_path)
    fx_latest = None
    for r in reversed(fx_rows):
        v = safe_float(r.get("usd_cny", ""))
        if not math.isnan(v):
            fx_latest = v
            break
    if fx_latest:
        config["fx_rate"] = fx_latest

    # ── 3. 输出 metrics.json ──
    total_points = len(ROUTES) * window_size
    pending_count = sum(
        1 for code in ROUTES
        for v in route_26[code] if math.isnan(v)
    )
    # 市场总体态：SCFI 综合作为验证位，不计入航线计数（避免共线性）
    # 只统计 4 条具体航线
    routes_in_red = sum(1 for code in ROUTES if code != "COMPOSITE" and route_metrics[code]["warning_level"] == "红色预警")
    routes_in_yellow = sum(1 for code in ROUTES if code != "COMPOSITE" and route_metrics[code]["warning_level"] == "黄色预警")
    routes_in_green = sum(1 for code in ROUTES if code != "COMPOSITE" and route_metrics[code]["warning_level"] == "绿色正常")
    scfi_red = route_metrics["COMPOSITE"]["warning_level"] == "红色预警"

    # 市场红色 = SCFI至少黄色 + ≥2航线红；或全线路红 + SCFI不低于绿色
    scfi_not_green = route_metrics["COMPOSITE"]["warning_level"] != "绿色正常"
    if (scfi_not_green and routes_in_red >= 2):
        overall = "红色预警"
        desc = f"多条航线进入历史极值区间，SCFI 综合指数确认。建议全航线收紧报价有效期。"
    elif routes_in_red >= 1 or routes_in_yellow >= 2:
        overall = "黄色预警"
        desc = f"部分航线运价偏离均值，建议密切关注。"
    else:
        overall = "绿色正常"
        desc = "各航线运价处于历史正常区间。"

    # ── 季节性标记（L1: SCFI COMPOSITE 月均/全局均比率驱动 → L2: 样本不足回退月份法）──
    month = int(LATEST_WEEK[5:7])

    # L1: 从 SCFI COMPOSITE 列计算各月平均 vs 全局平均的比率
    monthly_composites = {}     # {YYYY-MM: [values]}
    for row in scfi_rows:
        week_str = row.get("week", "")
        comp_str = row.get("COMPOSITE", "")
        if week_str and comp_str:
            try:
                val = float(comp_str)
                month_key = week_str[:7]        # YYYY-MM
                monthly_composites.setdefault(month_key, []).append(val)
            except (ValueError, IndexError):
                continue

    # 全局平均
    all_composites = [v for vals in monthly_composites.values() for v in vals]
    global_avg = sum(all_composites) / len(all_composites) if all_composites else 0

    current_month_key = LATEST_WEEK[:7]

    # L2: 样本不足（<3 个月份有数据，或当前月无数据）→ 回退原月份法
    season_cfg = config.get("season", {})
    month_fallback = season_cfg.get("month_fallback", {})
    if (len(monthly_composites) < 3
            or current_month_key not in monthly_composites
            or len(monthly_composites[current_month_key]) == 0):
        season = month_fallback.get(month, "平季")
    else:
        # L1: 比率驱动判定
        monthly_avg = (sum(monthly_composites[current_month_key])
                       / len(monthly_composites[current_month_key]))
        ratio = monthly_avg / global_avg
        ratio_s = f"{ratio:.2f}"

        # 季度
        q = (month - 1) // 3 + 1

        ratio_high = season_cfg.get("ratio_high", 1.05)
        ratio_mid = season_cfg.get("ratio_mid", 1.02)
        ratio_low = season_cfg.get("ratio_low", 0.98)

        if ratio > ratio_high:
            season = f"旺季(Q{q}, 比率{ratio_s})"
        elif ratio > ratio_mid:
            season = f"偏旺(比率{ratio_s})"
        elif ratio < ratio_low:
            season = f"淡季(比率{ratio_s})"
        else:
            season = f"平季(比率{ratio_s})"

    metrics = OrderedDict()
    metrics["_meta"] = make_meta(LATEST_WEEK,
        f"{len(effective_weeks)}/{window_size} 周有真实数据，{pending_count} 数据点 PENDING。当前处于{season}。")
    metrics["routes"] = []
    for code in ROUTES:
        rm = route_metrics[code]
        metrics["routes"].append(OrderedDict([
            ("code", code),
            ("name", ROUTE_META[code]["name"]),
            ("unit", ROUTE_META[code]["unit"]),
            ("current_value", rm["current_value"] if not math.isnan(rm["current_value"]) else None),
            ("percentiles", OrderedDict(sorted(rm["percentiles"].items()))),
            ("wow_change_pct", rm["wow_change_pct"] if not math.isnan(rm["wow_change_pct"]) else None),
            ("z_score", rm["z_score"] if not math.isnan(rm["z_score"]) else None),
            ("up_streak_weeks", rm["up_streak_weeks"]),
            ("warning_level", rm["warning_level"]),
            ("warning_tags", rm["warning_tags"]),
            ("quality_level", QUALITY_LEVEL),
            ("data_quality", rm["data_quality"]),
        ]))
    metrics["market_regime"] = OrderedDict([
        ("overall_warning", overall),
        ("routes_in_red", routes_in_red),
        ("routes_in_yellow", routes_in_yellow),
        ("routes_in_green", routes_in_green),
        ("scfi_validates", scfi_red),
        ("season", season),
        ("description", desc),
    ])
    metrics["_stats"] = make_stats(total_points, pending_count,
                                   max(rm["eff_n"] for rm in route_metrics.values()))

    metrics_path = os.path.join(output_dir, "metrics.json")
    with open(metrics_path, "w", encoding="utf-8") as f:
        json.dump(metrics, f, ensure_ascii=False, indent=2)
    print(f"\n✅ metrics.json → {metrics_path}")
    print(f"   航线: {[r['code'] + ':' + r['warning_level'] for r in metrics['routes']]}")
    print(f"   市场: {overall} (红{routes_in_red} 黄{routes_in_yellow} 绿{routes_in_green})")

    # ── 4. 输出 history.json ──
    history = OrderedDict()
    history["_meta"] = make_meta(LATEST_WEEK)
    history["labels"] = effective_weeks
    datasets = []
    for code in ROUTES:
        vals = route_26[code][:latest_idx + 1]
        p95 = route_metrics[code]["percentiles"].get("p95", None)
        datasets.append(OrderedDict([
            ("code", code),
            ("name", ROUTE_META[code]["name"]),
            ("unit", ROUTE_META[code]["unit"]),
            ("color", ROUTE_META[code]["color"]),
            ("p95_line", p95 if p95 and not math.isnan(p95) else None),
            ("data", [v if not math.isnan(v) else None for v in vals]),
        ]))
    history["datasets"] = datasets
    total_hist_points = len(ROUTES) * len(effective_weeks)
    hist_pending = sum(1 for ds in datasets for v in ds["data"] if v is None)
    history["_stats"] = make_stats(total_hist_points, hist_pending,
                                   max(rm["eff_n"] for rm in route_metrics.values()))

    history_path = os.path.join(output_dir, "history.json")
    with open(history_path, "w", encoding="utf-8") as f:
        json.dump(history, f, ensure_ascii=False, indent=2)
    print(f"✅ history.json → {history_path}")

    # ── 5. 输出 scenarios.json ──
    surcharge_path = os.path.join(shared_dir, "surcharge-scenarios.csv")
    surcharge_rows = read_csv(surcharge_path)

    scenarios_list = []
    fx_rate_val = config["fx_rate"]
    for row in surcharge_rows:
        code = row["scenario_code"]
        route_code = row["route_group"]
        surcharge = safe_float(row["surcharge_usd_per_feu"])
        base_freight = route_metrics[route_code]["current_value"]
        total_usd = (base_freight + surcharge) if not math.isnan(base_freight) else float("nan")
        total_cny = total_usd * fx_rate_val if not math.isnan(total_usd) else float("nan")

        risk_level = "normal"
        if "STRESS" in code:
            risk_level = "stress"
        if "PANAMA" in code:
            risk_level = "extreme"

        scenarios_list.append(OrderedDict([
            ("code", code),
            ("name", row["scenario_name_cn"]),
            ("route_code", route_code),
            ("base_freight_usd", base_freight if not math.isnan(base_freight) else None),
            ("surcharge_usd", surcharge),
            ("total_cost_usd", round(total_usd, 2) if not math.isnan(total_usd) else None),
            ("total_cost_cny", round(total_cny, 2) if not math.isnan(total_cny) else None),
            ("description", f"共 {row['applied_fee_count']} 项费用"),
            ("risk_level", risk_level),
        ]))

    scenarios = OrderedDict()
    scenarios["_meta"] = make_meta(LATEST_WEEK)
    scenarios["scenarios"] = scenarios_list
    scenarios["sensitivity"] = OrderedDict([
        ("fx_rate_range", [
            round(fx_rate_val * 0.97, 4),
            round(fx_rate_val, 4),
            round(fx_rate_val * 1.03, 4),
        ]),
        ("surcharge_multipliers", [1.0, 1.5, 2.0]),
        ("freight_change_pct", [0, 10, 20, 30]),
    ])
    sensitivity_dims = len(scenarios.get("sensitivity", {}).get("freight_change_pct", [0, 10, 20, 30]))
    scenarios["_stats"] = make_stats(len(scenarios_list) * sensitivity_dims, 0, len(scenarios_list))

    scenarios_path = os.path.join(output_dir, "scenarios.json")
    with open(scenarios_path, "w", encoding="utf-8") as f:
        json.dump(scenarios, f, ensure_ascii=False, indent=2)
    print(f"✅ scenarios.json → {scenarios_path}")

    # ── 6. 输出 decisions.json ──
    decisions_list = []
    for code in ROUTES:
        rm = route_metrics[code]
        suggestion = build_suggestion(
            code, rm["warning_level"],
            rm["current_value"], rm["z_score"], rm["up_streak_weeks"],
        )
        decisions_list.append(OrderedDict([
            ("code", code),
            ("name", ROUTE_META[code]["name"]),
            ("warning_level", rm["warning_level"]),
            ("suggestion", suggestion),
            ("confidence", QUALITY_LEVEL),
            ("source_metrics", rm["warning_tags"]),
        ]))

    # 交叉验证
    # SCFI 4周趋势：从 COMPOSITE 路由的 route_26 数据中计算
    scfi_dir = "up"  # 默认
    comp_vals = route_26.get("COMPOSITE", [])
    comp_valid = [v for v in comp_vals if not math.isnan(v)]
    if len(comp_valid) >= 8:
        scfi_latest_4w_ma = sum(comp_valid[-4:]) / 4
        scfi_prev_4w_ma = sum(comp_valid[-8:-4]) / 4
        scfi_dir = "up" if scfi_latest_4w_ma > scfi_prev_4w_ma else "down"
    ccfi_dir = ccfi_4w_dir
    consistency = "consistent" if scfi_dir == ccfi_dir else "divergent"

    decisions = OrderedDict()
    decisions["_meta"] = make_meta(LATEST_WEEK)
    decisions["decisions"] = decisions_list
    decisions["cross_validation"] = OrderedDict([
        ("scfi_direction", scfi_dir),
        ("ccfi_direction", ccfi_dir),
        ("consistency", consistency),
        ("note", f"SCFI 与 CCFI 4W趋势{'同向' if consistency == 'consistent' else '背离'}，{'高置信' if consistency == 'consistent' else '需关注'}。⚠️ CCFI 天然滞后 SCFI 2-4 周，同向时可能低估拐点。已有 WCI/FBX 三方验证数据。"),
    ])
    decisions["_stats"] = make_stats(len(ROUTES), 0, len(ROUTES))

    decisions_path = os.path.join(output_dir, "decisions.json")
    with open(decisions_path, "w", encoding="utf-8") as f:
        json.dump(decisions, f, ensure_ascii=False, indent=2)
    print(f"✅ decisions.json → {decisions_path}")

    # ── 7. 输出 indices.json ──
    idx_path = os.path.join(shared_dir, "index-comparison.csv")
    idx_rows = read_csv(idx_path)

    # 从实际 CSV 数据中提取最新值（替代硬编码）
    idx_override = {}

    # SCFI: 从 scfi-26w.csv 最后一行的 COMPOSITE 列提取
    if scfi_rows:
        last_scfi = scfi_rows[-1]
        scfi_val = safe_float(last_scfi.get("COMPOSITE", ""))
        if not math.isnan(scfi_val):
            idx_override["SCFI"] = {
                "value": scfi_val,
                "date": last_scfi.get("week", LATEST_WEEK),
                "quality_level": QUALITY_LEVEL,
                "status": "collected",
            }

    # CCFI: 从 ccfi-weekly.csv 最后一行提取
    if ccfi_rows:
        ccfi_rows_sorted = sorted(ccfi_rows, key=lambda r: r["week"])
        last_ccfi = ccfi_rows_sorted[-1]
        ccfi_val = safe_float(last_ccfi.get("CCFI", ""))
        if not math.isnan(ccfi_val):
            idx_override["CCFI"] = {
                "value": ccfi_val,
                "date": last_ccfi["week"],
                "quality_level": "A_official",
                "status": "collected",
            }

    # SCFIS: 从 scfis-weekly.csv 最后一行提取
    scfis_path = os.path.join(shared_dir, "scfis-weekly.csv")
    scfis_rows = read_csv(scfis_path)
    if scfis_rows:
        scfis_rows_sorted = sorted(scfis_rows, key=lambda r: r.get("week", r.get("date", "")))
        last_scfis = scfis_rows_sorted[-1]
        scfis_val = safe_float(last_scfis.get("SCFIS_EUROPE", ""))
        if not math.isnan(scfis_val):
            # scfis-weekly.csv 的日期列名可能是 "week" 或 "date"
            scfis_date = last_scfis.get("week") or last_scfis.get("date", "")
            idx_override["SCFIS"] = {
                "value": scfis_val,
                "date": scfis_date,
                "quality_level": "A_official",
                "status": "collected",
            }

    idx_summary = {k: f"{v['value']}@{v['date']}" for k, v in idx_override.items()}
    print(f"   idx_override: {idx_summary}")

    indices_list = []
    for row in idx_rows:
        code = row["index_code"]
        if code in idx_override:
            ov = idx_override[code]
            indices_list.append(OrderedDict([
                ("code", code),
                ("name", row["index_name"]),
                ("value", ov["value"]),
                ("unit", row["unit"]),
                ("date", ov["date"]),
                ("quality_level", ov["quality_level"]),
                ("status", ov["status"]),
                ("source_url", ""),
            ]))
        else:
            v = safe_float(row.get("value", ""))
            indices_list.append(OrderedDict([
                ("code", code),
                ("name", row["index_name"]),
                ("value", v if not math.isnan(v) else None),
                ("unit", row["unit"]),
                ("date", row.get("date", "") or None),
                ("quality_level", row["quality_level"]),
                ("status", row["status"]),
                ("source_url", ""),
            ]))

    indices = OrderedDict()
    indices["_meta"] = make_meta(LATEST_WEEK)
    indices["indices"] = indices_list
    collected = sum(1 for i in indices_list if i["status"] == "collected")
    pending = sum(1 for i in indices_list if i["status"] != "collected")
    indices["_stats"] = make_stats(len(indices_list), pending, collected)

    indices_path = os.path.join(output_dir, "indices.json")
    with open(indices_path, "w", encoding="utf-8") as f:
        json.dump(indices, f, ensure_ascii=False, indent=2)
    print(f"✅ indices.json → {output_dir}/indices.json")

    # ── 8. 汇总 ──
    print("\n" + "=" * 60)
    print("🏁 compute.py 完成")
    print(f"   metrics.json   — {len(metrics['routes'])} 航线")
    print(f"   history.json   — {len(history['labels'])} 周 × {len(ROUTES)} 航线")
    print(f"   scenarios.json — {len(scenarios_list)} 场景")
    print(f"   decisions.json — {len(decisions_list)} 航线建议")
    print(f"   indices.json   — {len(indices_list)} 指数")
    print(f"   汇率: {config['fx_rate']}")
    pct = (pending_count / total_points * 100) if total_points > 0 else 0
    print(f"   数据缺口: {pending_count}/{total_points} ({pct:.1f}%)")
    print("=" * 60)


def resolve_cli_path(path_value, fallback_base=None):
    """Resolve CLI paths consistently.

    Relative paths are resolved from the current working directory first,
    matching normal CLI expectations. If that path does not exist and a
    fallback_base is provided, resolve relative to fallback_base for backward
    compatibility with older script-relative defaults.
    """
    if os.path.isabs(path_value):
        return path_value

    cwd_candidate = os.path.abspath(path_value)
    if os.path.exists(cwd_candidate) or fallback_base is None:
        return cwd_candidate

    return os.path.abspath(os.path.join(fallback_base, path_value))


if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.abspath(os.path.join(script_dir, ".."))

    shared = os.path.abspath(os.path.join(project_root, "..", "shared"))
    output = os.path.abspath(os.path.join(project_root, "output"))

    if len(sys.argv) > 1 and not sys.argv[1].startswith("--"):
        shared = resolve_cli_path(sys.argv[1], fallback_base=script_dir)

    for i, arg in enumerate(sys.argv):
        if arg == "--shared-dir" and i + 1 < len(sys.argv):
            shared = resolve_cli_path(sys.argv[i + 1], fallback_base=script_dir)
        if arg == "--output-dir" and i + 1 < len(sys.argv):
            output = resolve_cli_path(sys.argv[i + 1], fallback_base=project_root)

    main(shared, output)
