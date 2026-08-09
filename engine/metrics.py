"""
舱路雷达 · metrics.py
统计计算函数：percentile / calc_stats / up_streak_count / warning_level / warning_tags
从 compute.py v5.3 抽离，严格保持行为一致
"""

import math


def percentile(sorted_vals, p):
    """线性插值百分位数"""
    if not sorted_vals:
        return float("nan")
    k = (len(sorted_vals) - 1) * p / 100.0
    f = math.floor(k)
    c = math.ceil(k)
    if f == c:
        return sorted_vals[int(k)]
    d0 = sorted_vals[int(f)] * (c - k)
    d1 = sorted_vals[int(c)] * (k - f)
    return d0 + d1


def calc_stats(values):
    """计算均值、标准差（仅非 NaN）"""
    valid = [v for v in values if not math.isnan(v)]
    if not valid:
        return float("nan"), float("nan"), 0
    mean = sum(valid) / len(valid)
    if len(valid) < 2:
        return mean, float("nan"), len(valid)
    var = sum((v - mean) ** 2 for v in valid) / (len(valid) - 1)
    return mean, math.sqrt(var), len(valid)


def up_streak_count(route_values):
    """计算连续上涨周数（从最新非 NaN 往前数，NaN 断连涨）"""
    streak = 0
    prev = None
    for v in reversed(route_values):
        if math.isnan(v):
            break  # 数据缺失 → 连涨中断
        if prev is None:
            prev = v
            streak = 1
        elif v < prev:
            streak += 1
            prev = v
        else:
            break
    return streak


def warning_level(z_score, up_streak, current_val, p95, p85, wow_pct,
                  route_code="COMPOSITE", data_quality="full",
                  surge_thresholds=None,
                  z_red=2.0, z_red_b=1.8, z_yellow=1.5):
    """预警等级判定（含单周暴涨快通道 + 趋势钝化缓解 + 数据降级）"""
    if surge_thresholds is None:
        surge_thresholds = {"USWC": 20, "USEC": 18, "EUR": 15, "MED": 15}
    if math.isnan(current_val):
        return "灰色-数据缺失"
    # 🔴 快通道：单周极端涨幅直接红色，不经三重AND
    #    阈值按航线波动特征差异化：美西/美东波动大→20%，欧/地/综合平稳→15%
    surge_threshold = surge_thresholds.get(route_code, 15)
    if not math.isnan(wow_pct) and wow_pct >= surge_threshold:
        return "红色预警"
    # 🔴 标准通道A：三重AND（Z + 连涨 + P95）
    if z_score >= z_red and up_streak >= 3:
        if not math.isnan(p95) and current_val >= p95:
            return "红色预警"
    # 🔴 标准通道B：趋势钝化缓解（Z≥1.8 + 连涨≥3 + ≥P85）
    #    解决缓慢持续上涨中 Z 被均值吞噬的问题
    #    连涨≥3（非2）避免美西正常波动误触发
    if (not math.isnan(z_score) and z_score >= z_red_b) and up_streak >= 3:
        if not math.isnan(p85) and current_val >= p85:
            return "红色预警"
    # 🟡 黄色：Z≥1.5 或（P85高位 + 连涨≥1），避免单条件过于宽松
    if (not math.isnan(z_score) and z_score >= z_yellow):
        return "黄色预警"
    if (not math.isnan(p85) and current_val >= p85) and up_streak >= 1:
        return "黄色预警"
    # 🟢 绿色
    return "绿色正常"


def warning_tags(z_score, current_val, p95, p85, up_streak, wow_pct):
    """生成 warning_tags（决策规则 §二）"""
    tags = []
    if not math.isnan(current_val):
        if not math.isnan(p95) and current_val >= p95:
            tags.append("P95高位")
        elif not math.isnan(p85) and current_val >= p85:
            tags.append("P85高位")
    if not math.isnan(z_score) and z_score >= 2.0:
        tags.append("Z≥2异常")
    elif not math.isnan(z_score) and z_score >= 1.5:
        tags.append("Z≥1.5偏离")
    if up_streak >= 3:
        tags.append("连续上涨≥3周")
    if not math.isnan(wow_pct) and abs(wow_pct) >= 10:
        tags.append("周涨跌幅≥10%")
    elif not math.isnan(wow_pct) and abs(wow_pct) >= 5:
        tags.append("周涨跌幅≥5%")
    return tags
