# 舱路雷达｜原始数据接入清单

> 创建日期：2026-05-28  
> 用途：恢复项目后，承接真实公开数据接入；禁止使用 template 文件或手工虚构数值替代真实数据。

## 1. 接入总原则

- 所有原始数据先落入 `01-raw-data/` 对应子目录，再进入 `02-processed-data/` 治理。
- 每个数据文件必须能追溯来源：来源名称、URL/下载位置、抓取/下载日期、覆盖时间范围。
- 若来源为网页公告，应保留原文或截图/HTML 摘要，并另行抽取结构化字段。
- 模板文件仅用于字段说明，不得参与指标计算、趋势分析或报告结论。

## 2. 必需数据项

| 数据类别 | 目标目录 | 建议文件名 | 最低字段要求 | 验收条件 |
|---|---|---|---|---|
| 运价指数 | `01-raw-data/freight-index/` | `raw_freight_index.csv` | date, route_code, index_value, source_name, source_url | 至少覆盖近26周；包含中欧、亚欧或可映射航线 |
| 船司公告 | `01-raw-data/carrier-announcements/` | `raw_carrier_announcements.csv` | publish_date, carrier, route, fee_type, amount, currency, effective_date, source_url | 至少3-5条公开公告；字段可回溯原文 |
| 附加费规则 | `01-raw-data/surcharge-rules/` | `raw_surcharge_rules.csv` | route_code, fee_type, trigger_condition, amount, currency, source_url | 与船司公告或公开规则一致 |
| 汇率 | `01-raw-data/exchange-rate/` | `raw_exchange_rate.csv` | date, currency_pair, rate, source_name, source_url | USD/CNY、EUR/CNY 至少覆盖近26周 |
| 航线字典 | `01-raw-data/route-dictionary/` | `raw_route_dictionary.csv` | route_code, origin_region, destination_region, alias, notes | 能支撑公告文本与运价指数的航线映射 |

## 3. 推荐接入顺序

1. 汇率：优先接入，字段结构简单，可先验证治理流程。
2. 航线字典：统一 `route_code`，避免后续多源数据无法关联。
3. 运价指数：接入后可生成趋势、波动率等核心指标。
4. 船司公告与附加费规则：接入后可抽取事件与风险信号。
5. 进入 `02-processed-data/`：按 `00-control/naming-rules.md` 进行字段规范化。

## 4. 当前状态

- `01-raw-data/` 目录结构已存在。
- 当前仅发现模板型文件，尚未发现可直接用于计算的真实原始数据。
- 已在 `09-logs/data-source-log.md` 记录候选数据源，待下载/抓取后更新为实际来源。
