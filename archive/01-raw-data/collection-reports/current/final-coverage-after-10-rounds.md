# 舱路雷达｜10轮搜索与数据录入后覆盖率报告

## 停止条件
- 已执行到第10轮搜索/录入流程，因此停止。
- 真实/公开数据整体覆盖率未达到95%。
- 含演示补全版整体覆盖率达到或超过95%，但其中 `C_demo` 不可用于正式分析。

## 覆盖率表

| layer | item | covered | total | coverage | difficulty_if_below_90 |
|---|---:|---:|---:|---:|---|
| true_public | SCFI_record | 18 | 26 | 69.23% | 剩余周次主要缺可复核原文/截图；航交所历史单期页常回显当前页或分航线为空。 |
| true_public | CCFI_record | 9 | 26 | 34.62% | CCFI可作为交叉指标，但历史周综合/分航线公开转载少，官方多期受限。 |
| true_public | SCFIS_record | 6 | 32 | 18.75% | SCFIS按周一发布/轨迹，与周五自然周对齐复杂；公开转载少且部分数值冲突。 |
| true_public | FX_weekly_record | 1 | 26 | 3.85% | SAFE/ChinaMoney历史日度表需要外部检索或页面访问；本轮联网搜索工具持续失败，不能用模拟值替代真实表。 |
| true_public | Carrier_event_key_fields | 19 | 20 | 95.00% | 仅剩MSC公告缺公告日期/原文URL；船司网页可能动态加载或需站内检索。 |
| demo_completed | SCFI_record | 26 | 26 | 100.00% |  |
| demo_completed | CCFI_record | 26 | 26 | 100.00% |  |
| demo_completed | SCFIS_record | 32 | 32 | 100.00% |  |
| demo_completed | FX_weekly_record | 26 | 26 | 100.00% |  |
| demo_completed | Carrier_event_key_fields | 20 | 20 | 100.00% |  |
| demo_completed | OVERALL | 130 | 130 | 100.00% |  |
| true_public | OVERALL | 53 | 130 | 40.77% |  |

## 单项覆盖率低于90%的具体困难点

- **SCFI_record：69.23%**。困难点：剩余周次主要缺可复核原文/截图；航交所历史单期页常回显当前页或分航线为空。
- **CCFI_record：34.62%**。困难点：CCFI可作为交叉指标，但历史周综合/分航线公开转载少，官方多期受限。
- **SCFIS_record：18.75%**。困难点：SCFIS按周一发布/轨迹，与周五自然周对齐复杂；公开转载少且部分数值冲突。
- **FX_weekly_record：3.85%**。困难点：SAFE/ChinaMoney历史日度表需要外部检索或页面访问；本轮联网搜索工具持续失败，不能用模拟值替代真实表。

## 重要说明
- A/B 真实或公开层与 `C_demo` 演示补全层分开维护。
- `C_demo` 仅用于跑通流程和展示覆盖，不得替代正式分析结论。
- 本轮外部 `web_search` 多次返回 `MCP tool execution failed`，是导致真实覆盖率无法继续提升的主要限制之一。