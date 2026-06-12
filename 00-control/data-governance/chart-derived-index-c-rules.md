# 舱路雷达｜图表反推指数数据 C 级治理规则

## 1. 适用场景
当上海航运交易所或其他公开网页只提供趋势图、折线图、鼠标悬停 tooltip、截图证据，而没有可直接下载或复制的官方数值表时，可以将图表识别结果作为 C 级参考数据留存。

## 2. 数据分层
- `A`：官方网页/官方表格/官方公告中可直接复核的结构化数值。
- `B`：公开转载、媒体正文、行业网站正文中可复核的数值。
- `C_chart_reference`：从网页图表截图、tooltip、坐标网格、曲线位置反推得到的参考数值。
- `PENDING`：仅有线索但无可复核数值，或截图/图表不足以判断。

## 3. C 级图表数据的两种细分
1. `tooltip_reading_from_screenshot`：截图中 tooltip 明确显示日期和值。可记录为 C 级参考，置信度高于网格估读。
2. `grid_estimation_from_chart`：根据坐标轴、网格线、曲线位置估算。必须保留估算区间或误差说明，不得写成官方精确值。

## 4. 入表原则
- C 级图表数据不得覆盖 A/B 级真实主表字段。
- C 级图表数据应进入 `collection-drafts/chart-evidence/chart-derived-index-records.csv`。
- 如需用于演示、建模或补全曲线，应进入演示层/参考层，并显著标注 `C_chart_reference`。
- 如果同一日期后续获得 A/B 级数值，应保留 C 级截图证据，但正式分析优先采用 A/B。

## 5. 必填字段
- `index_type`
- `route_or_dimension`
- `data_date`
- `natural_week_start`
- `natural_week_end`
- `displayed_value` 或 `estimated_value`
- `value_extraction_method`
- `evidence_file`
- `data_quality_level`
- `record_status`
- `confidence_note`
- `usable_for_real_master`

## 6. 证据留存
截图统一存放在：

`canglu-radar/01-raw-data/collection-drafts/chart-evidence/`

视觉识别/人工校验说明应与截图同目录保存。后续若使用浏览器复现页面，应补充页面 URL、访问日期、截图时间和页面正文/HTML缓存。

## 7. 当前已确认的示例
- CCFI 综合指数图表 tooltip：2026-05-22，1317.36。
- SCFIS 欧洲航线图表 tooltip：2026-05-25，1863.74。
- SCFIS 美西航线图表 tooltip：2026-05-25，1960.27。

## 8. 航运指数后续采集策略调整
用户确认：部分航运历史数据人工也难以查得，后续 SCFI/CCFI/SCFIS 等航运指数缺口可按网页图表、tooltip、坐标估读进入 `C_chart_reference` 层。该层可用于趋势展示、演示补全和辅助建模，但不得冒充 A/B 官方或公开正文数值。
