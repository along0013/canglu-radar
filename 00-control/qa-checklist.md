# 舱路雷达｜质量检查清单

## 数据一致性

- [ ] 日期格式统一为 YYYY-MM-DD
- [ ] 航线代码仅使用 CN-USWC、CN-USEC、CN-EUR
- [ ] 运价和费用统一为 USD/FEU
- [ ] 字段列名与规范一致
- [ ] CR-04A中的数字与CR-05、CR-06、CR-07一致

## 合规声明

- [ ] 公开数据标注来源
- [ ] 脱敏数据说明处理方式
- [ ] 模拟数据明确声明“仅用于演示工作流能力”
- [ ] 公告关联只写“高置信关联线索”或“中等关联线索”
- [ ] 不写确定因果关系

## 交付检查

- [ ] 文件命名符合CR规范
- [ ] 每批次输出文件齐全
- [ ] Excel公式可复核
- [ ] Word/PPT标题结论先行
- [ ] 提交目录与CR-10C一致

## 7天冲刺一致性QA补充

| 检查项 | 状态 | 说明 |
|---|---|---|
| 数字一致性 | PASS_PARTIAL | CR-04A为唯一数字源，CR-04B/CR-05/PPT脚本均引用同一批计算结果；PPTX尚未生成，需后续核对。 |
| 数据质量等级标注 | PASS | CR-04A每行含quality_level；C_demo_interpolation未升级为A。 |
| 公告关联措辞 | PASS | CR-05仅使用“关联线索”，未写确定因果。 |
| 模拟/参考数据声明 | PASS | 附加费明确为C_market_reference；视频录制和外部补采为PENDING。 |
| 复跑路径完整性 | PASS_PARTIAL | 已生成3次dry-run复跑记录；未完成真实连续三周运营。 |
| 工具整合证据 | PASS_PARTIAL | 已覆盖数据分析、Excel、Word报告、PPT storyboard、长图、Demo脚本、QA、打包；正式PPTX/Demo视频待补。 |

## 七天冲刺一致性检查补充

- [x] CR-04A 已生成，作为唯一数字源。
- [x] CR-04B 决策建议已引用 CR-04A 数字。
- [x] CR-05 分析报告已生成，并声明数据质量边界。
- [x] 场景化附加费模型已替代简单合计。
- [x] CR-06 storyboard 已补齐 P6-P8。
- [x] CR-06 HTML-first 展示源已生成。
- [ ] CR-06 PPTX 导出：PENDING_EXPORT，受当前环境 Playwright Chromium / PptxGenJS 依赖限制。
- [x] CR-07 长图已生成。
- [x] CR-08 Demo脚本已生成。
- [x] CR-09 量化验证表已生成，真实缺失项保留 PENDING。
- [x] Week1/Week2/Week3 复跑记录已生成；说明为模拟复跑验证，不冒充真实连续三周生产运行。
- [x] 全文因果表述已规避确定因果判断。
