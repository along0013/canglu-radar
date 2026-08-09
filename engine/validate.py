#!/usr/bin/env python3
"""
舱路雷达 · validate.py
对 compute.py 输出的 5 个 JSON 执行 6 条跨文件一致性约束 + 值域检查
严格遵循 specs/data-format-v5.md §四 + §五

用法: python3 validate.py [--data-dir PATH]
退出码: 0 = 全部通过, 1 = 存在 ERROR, 2 = 仅 WARNING
"""

import json
import math
import os
import sys

# ── 配置 ──────────────────────────────────────────────────
ROUTES = {"EUR", "MED", "USWC", "USEC", "COMPOSITE"}
VALID_WARNINGS = {"红色预警", "黄色预警", "绿色正常", "灰色-数据缺失", "灰色-数据不足"}
FILES = ["metrics.json", "history.json", "scenarios.json", "decisions.json", "indices.json"]

# ── 结果收集 ──────────────────────────────────────────────
errors = []
warnings = []

def err(msg):
    errors.append(msg)
    print(f"  ❌ ERROR: {msg}")

def warn(msg):
    warnings.append(msg)
    print(f"  ⚠️  WARNING: {msg}")

def ok(msg):
    print(f"  ✅ {msg}")


def load_json(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def main(data_dir="data"):
    print("=" * 60)
    print("舱路雷达 · validate.py")
    print(f"  数据目录: {data_dir}")
    print("=" * 60)

    # ── 加载所有 JSON ──
    jsons = {}
    for fname in FILES:
        fpath = os.path.join(data_dir, fname)
        if not os.path.exists(fpath):
            err(f"文件缺失: {fname}")
            continue
        jsons[fname] = load_json(fpath)

    if errors:
        print(f"\n❌ {len(errors)} 个致命错误（文件缺失），无法继续。")
        sys.exit(1)

    m = jsons["metrics.json"]
    h = jsons["history.json"]
    s = jsons["scenarios.json"]
    d = jsons["decisions.json"]
    idx = jsons["indices.json"]

    # ═══════════════════════════════════════════════════════
    # C1: 时间基线 — 所有 JSON _meta.latest_week 一致
    # ═══════════════════════════════════════════════════════
    print("\n── C1 时间基线 ──")
    lw_values = {}
    for name, j in jsons.items():
        lw = j.get("_meta", {}).get("latest_week")
        lw_values[name] = lw
        print(f"  {name}: latest_week={lw}")

    ref_lw = lw_values.get("metrics.json")
    if ref_lw:
        for name, lw in lw_values.items():
            if lw != ref_lw:
                err(f"C1: {name} latest_week={lw} ≠ metrics.json={ref_lw}")
    if not any(e.startswith("C1:") for e in errors):
        ok("C1 时间基线一致")

    # ═══════════════════════════════════════════════════════
    # C2: 航线集合一致
    # ═══════════════════════════════════════════════════════
    print("\n── C2 航线集合 ──")
    metrics_codes = {r["code"] for r in m.get("routes", [])}
    decisions_codes = {d["code"] for d in d.get("decisions", [])}
    history_codes = {ds["code"] for ds in h.get("datasets", [])}

    print(f"  metrics:   {sorted(metrics_codes)}")
    print(f"  decisions: {sorted(decisions_codes)}")
    print(f"  history:   {sorted(history_codes)}")

    if metrics_codes != ROUTES:
        err(f"C2: metrics 航线集合 {metrics_codes} ≠ 期望 {ROUTES}")
    if decisions_codes != ROUTES:
        err(f"C2: decisions 航线集合 {decisions_codes} ≠ 期望 {ROUTES}")
    if history_codes != ROUTES:
        err(f"C2: history 航线集合 {history_codes} ≠ 期望 {ROUTES}")

    if not any(e.startswith("C2:") for e in errors):
        ok("C2 航线集合一致")

    # ═══════════════════════════════════════════════════════
    # C3: 运价锚点 — metrics.current_value = history 最后一个非 null
    # ═══════════════════════════════════════════════════════
    print("\n── C3 运价锚点 ──")
    for route in m.get("routes", []):
        code = route["code"]
        mv = route.get("current_value")
        # 找 history 对应航线的最后一个非 null
        ds = next((x for x in h.get("datasets", []) if x["code"] == code), None)
        if ds is None:
            err(f"C3: history 中找不到 {code}")
            continue
        last_valid = None
        for v in reversed(ds["data"]):
            if v is not None:
                last_valid = v
                break
        if mv is None and last_valid is None:
            ok(f"C3 {code}: 均为 null（PENDING）")
        elif mv != last_valid:
            err(f"C3 {code}: metrics.current_value={mv} ≠ history last_valid={last_valid}")
        else:
            ok(f"C3 {code}: {mv} ✓")

    # ═══════════════════════════════════════════════════════
    # C4: 场景锚点 — scenarios.base_freight_usd = metrics 同航线 current_value
    # ═══════════════════════════════════════════════════════
    print("\n── C4 场景锚点 ──")
    metrics_by_code = {r["code"]: r for r in m.get("routes", [])}
    for sc in s.get("scenarios", []):
        route_code = sc["route_code"]
        bf = sc.get("base_freight_usd")
        mr = metrics_by_code.get(route_code)
        if mr is None:
            err(f"C4: 场景 {sc['code']} 引用的航线 {route_code} 不在 metrics 中")
            continue
        cv = mr.get("current_value")
        if bf is None and cv is None:
            ok(f"C4 {sc['code']}: 均为 null")
        elif bf != cv:
            err(f"C4 {sc['code']}: base_freight_usd={bf} ≠ metrics.{route_code}.current_value={cv}")
        else:
            ok(f"C4 {sc['code']}: {bf} ✓")

    # ═══════════════════════════════════════════════════════
    # C5: 预警一致性 — metrics.warning_level ≡ decisions 同航线
    # ═══════════════════════════════════════════════════════
    print("\n── C5 预警一致性 ──")
    decisions_by_code = {d["code"]: d for d in d.get("decisions", [])}
    for route in m.get("routes", []):
        code = route["code"]
        mwl = route.get("warning_level")
        dd = decisions_by_code.get(code)
        if dd is None:
            err(f"C5: decisions 中找不到 {code}")
            continue
        dwl = dd.get("warning_level")
        if mwl != dwl:
            err(f"C5 {code}: metrics.warning_level={mwl} ≠ decisions.warning_level={dwl}")
        else:
            ok(f"C5 {code}: {mwl} ✓")

    # ═══════════════════════════════════════════════════════
    # C6: 汇率一致性 — 所有 JSON fx_rate 一致
    # ═══════════════════════════════════════════════════════
    print("\n── C6 汇率一致性 ──")
    fx_values = {}
    for name, j in jsons.items():
        fx = j.get("_meta", {}).get("fx_rate")
        fx_values[name] = fx
        print(f"  {name}: fx_rate={fx}")

    ref_fx = fx_values.get("metrics.json")
    if ref_fx:
        for name, fx in fx_values.items():
            if fx != ref_fx:
                err(f"C6: {name} fx_rate={fx} ≠ metrics.json={ref_fx}")
    if not any(e.startswith("C6:") for e in errors):
        ok("C6 汇率一致")

    # ═══════════════════════════════════════════════════════
    # 值域约束
    # ═══════════════════════════════════════════════════════
    print("\n── 值域约束 ──")

    # Z-score [-5.0, 10.0]
    for route in m.get("routes", []):
        z = route.get("z_score")
        if z is not None and (z < -5.0 or z > 10.0):
            warn(f"Z-score: {route['code']} z_score={z} 超出 [-5, 10]")
    ok("Z-score 范围检查")

    # WoW [-50, 50]
    for route in m.get("routes", []):
        w = route.get("wow_change_pct")
        if w is not None and (w < -50 or w > 50):
            warn(f"WoW: {route['code']} wow_change_pct={w} 超出 [-50, 50]")
    ok("WoW 范围检查")

    # up_streak [0, 26]
    for route in m.get("routes", []):
        s_val = route.get("up_streak_weeks")
        if s_val is not None and (s_val < 0 or s_val > 26):
            err(f"up_streak: {route['code']} up_streak_weeks={s_val} 超出 [0, 26]")
    ok("up_streak 范围检查")

    # percentiles 单调性
    pcts_order = ["p50", "p75", "p85", "p90", "p95"]  # compute.py 仅生成到 p95，不检查 p99
    for route in m.get("routes", []):
        pcts = route.get("percentiles", {})
        prev = None
        for pkey in pcts_order:
            val = pcts.get(pkey)
            if val is None:
                continue
            if prev is not None and val < prev:
                err(f"Percentile单调性: {route['code']} {pkey}={val} < 前值={prev}")
            prev = val
    ok("Percentile 单调性检查")

    # warning_level enum
    for route in m.get("routes", []):
        wl = route.get("warning_level")
        if wl not in VALID_WARNINGS:
            err(f"warning_level: {route['code']} = '{wl}' 不在 {VALID_WARNINGS}")
    ok("warning_level 枚举检查")

    # total_cost_cny ≈ total_cost_usd × fx_rate
    fx = m.get("_meta", {}).get("fx_rate", 6.8166)
    for sc in s.get("scenarios", []):
        usd = sc.get("total_cost_usd")
        cny = sc.get("total_cost_cny")
        if usd is None or cny is None:
            continue
        expected = usd * fx
        deviation = abs(cny - expected) / expected if expected != 0 else 0
        if deviation > 0.01:
            warn(f"CNY锚点: {sc['code']} total_cost_cny={cny} ≠ usd×fx={expected:.2f} (偏差{deviation*100:.2f}%)")
    ok("CNY 锚点检查")

    # pending_ratio [0, 1]
    for name, j in jsons.items():
        pr = j.get("_stats", {}).get("pending_ratio")
        if pr is not None and (pr < 0 or pr > 1):
            err(f"pending_ratio: {name} = {pr} 超出 [0, 1]")
    ok("pending_ratio 范围检查")

    # ── 汇总 ──
    print("\n" + "=" * 60)
    print(f"🏁 validate.py 完成")
    print(f"   ERROR:   {len(errors)}")
    print(f"   WARNING: {len(warnings)}")
    print("=" * 60)

    if errors:
        print("\n❌ 存在 ERROR — 需要修复后重新验证")
        sys.exit(1)
    elif warnings:
        print("\n⚠️  仅 WARNING — 建议关注但不阻塞")
        sys.exit(2)  # 退出码 2 = 仅 WARNING（与文档注释一致）
    else:
        print("\n✅ 全部通过 — 数据一致性无异常")
        sys.exit(0)


def resolve_data_dir(data_dir):
    """Resolve data_dir in a CLI-friendly way.

    Relative paths are resolved from the current working directory first,
    which matches normal CLI expectations such as running:

        python engine/validate.py --data-dir output

    from the project root. For backward compatibility, if the cwd-relative
    path does not exist, fall back to resolving relative to this script.
    """
    if os.path.isabs(data_dir):
        return data_dir

    cwd_candidate = os.path.abspath(data_dir)
    if os.path.exists(cwd_candidate):
        return cwd_candidate

    script_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(script_dir, data_dir)


if __name__ == "__main__":
    data_dir = "data"
    for i, arg in enumerate(sys.argv):
        if arg == "--data-dir" and i + 1 < len(sys.argv):
            data_dir = sys.argv[i + 1]

    main(resolve_data_dir(data_dir))
