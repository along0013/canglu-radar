# 复跑记录 Week 1

## 运行性质

本次为 dry-run：使用当前已有项目数据复跑完整计算链路，未伪造新增外部周数据。

## 输入文件

- `archive\current-data\canglu-freight-indicators-wide.csv`
- `archive\current-data\canglu-scfi-demo-filled-long.csv`
- `archive\current-data\canglu-fx-weekly-demo-aligned.csv`
- `..\canglu-radar\02-processed-data\canglu-demo-cost-model-scenario-based.csv`
- `..\canglu-radar\01-raw-data\carrier-announcements\carrier-announcements-natural-week-events.csv`

## 运行时间

- 运行耗时：0.014 秒
- 运行日期：2026-05-28

## 输出文件

- `03-analysis/CR-04A_指标计算结果.xlsx`
- `04-decision-report/CR-04B_业务决策建议.docx`
- `04-decision-report/CR-05_分析报告.docx`
- `05-presentation/CR-06_参赛展示PPT_storyboard.md`
- `06-visual-demo/CR-08_Demo演示脚本.docx`

## 关键数字摘要

```text
route_name  latest_value  max_value  red_count
  SCFI综合指数       2218.15    2218.15          2
     地中海航线       3207.00    3207.00          7
      欧洲航线       1905.00    1905.00          3
      美东航线       4313.00    4313.00          2
      美西航线       3154.00    3154.00          2
```

## 限制

- 未完成真实外部补采。
- 未替换最新周真实数据。
- 因此本记录可证明流程可复跑，但不能证明连续三周真实运营。
