# 舱路雷达｜二次优化执行报告

## 本轮目标

根据用户核验意见，集中修复五个高风险短板：

1. “假复跑”问题：补充 Week2' / Week3' 模拟真实复跑，输入和输出均发生变化；
2. CR-04B 航线建议一刀切问题：改为欧洲、地中海、美西、美东、SCFI综合差异化建议；
3. PPT正式形态不足：补充10页PNG截图包和可打印Markdown稿；
4. CR-04A公式审计为空：补充Excel公式审计示例和公式说明Sheet；
5. Demo视频素材不足：补充截图、旁白与字幕稿，保留PPTX/视频成片限制说明。

## 关键修复结果

### 1. 模拟真实复跑

新增复跑记录：

- `09-logs/rerun-records-week2-prime.md`
- `09-logs/rerun-records-week3-prime.md`

新增输入文件：

- `01-raw-data/freight-index/week2-input/`
- `01-raw-data/freight-index/week3-input/`
- `01-raw-data/exchange-rate/week2-input/`
- `01-raw-data/exchange-rate/week3-input/`
- `01-raw-data/carrier-announcements/week2-input/`
- `01-raw-data/carrier-announcements/week3-input/`

口径：全部明确标注为“模拟真实复跑”，用于验证系统响应输入变化，不冒充真实外部运营数据。

### 2. 差异化决策建议

主文件已更新：

- `04-decision-report/CR-04B_业务决策建议.docx`
- `04-decision-report/CR-05_分析报告.docx`
- `05-presentation/CR-06_参赛展示PPT_storyboard.md`

建议已按航线差异化：欧洲按TEU与亚欧节奏、地中海按高波动和替代港口、美西按跨境电商与订舱敏感、美东按成本基数和巴拿马路径、综合指数按全市场报价策略。

### 3. PPT与Demo素材

新增：

- `05-presentation/screenshots/demo-screenshot-P01.png` 至 `P10.png`
- `05-presentation/CR-06_可打印PPT稿.md`
- `05-presentation/printable-pages/`
- `05-presentation/PPT_EXPORT_NOTE.md`
- `06-visual-demo/demo-screenshots/`
- `06-visual-demo/demo-assets/demo-narration-subtitles.md`

说明：当前仍未声称已完成正式PPTX和视频成片，提交包以HTML源文件、PNG截图、可打印稿和旁白字幕稿作为替代交付。

### 4. 公式审计

`03-analysis/CR-04A_指标计算结果.xlsx` 已新增或补全：

- `Excel公式审计示例` Sheet；
- `公式说明` Sheet；
- 公式示例覆盖P95分位、周环比、Z分数、预警标签等；
- 当前工作簿包含可运行公式样例，避免“公式审计为空”。

## 仍未完全达标的地方

1. Week2'/Week3' 是模拟真实复跑，不是真实连续三周运营；
2. PPTX仍为 `PENDING_EXPORT`，但已补充HTML、截图和可打印稿；
3. Demo视频成片未录制，已补齐素材包和旁白字幕稿；
4. 新增复跑数据是人为构造输入状态，不能用于正式市场结论，只能用于机制验证。

## 最终提交包

- 路径：`08-submission/final-package/canglu-radar-submission.zip`
- 包内文件数：68

