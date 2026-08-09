"""
舱路雷达 · data_loader.py
数据读取与清洗函数：read_csv / safe_float
从 compute.py v5.3 抽离，严格保持行为一致
"""

import csv
import math
import os


def read_csv(path, strict=False):
    """读 CSV，处理 BOM，返回 list[dict]。strict=True 时文件缺失抛异常。"""
    rows = []
    if not os.path.exists(path):
        msg = f"  ⚠️ 文件不存在: {path}"
        if strict:
            raise FileNotFoundError(msg)
        print(msg)
        return rows
    with open(path, encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        for row in reader:
            # 清理空字符串
            cleaned = {k.strip(): v.strip() if v else "" for k, v in row.items()}
            rows.append(cleaned)
    return rows


def safe_float(v):
    """安全转 float，空值返回 NaN"""
    if v is None or v == "":
        return float("nan")
    try:
        return float(v)
    except (ValueError, TypeError):
        return float("nan")
