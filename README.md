# 舱路雷达 | 跨境物流异常预警与发货决策情报系统

舱路雷达是一个面向跨境电商物流运营的周度物流情报系统，用于把 SCFI 运价、船公司公告、汇率、附加费和场景化成本模型整合为可复跑的预警、建议、报告和展示材料。

## 一句话定位

用多源数据治理和自动化指标计算，替代物流专员“查网页、算 Excel、写建议、做汇报”的重复劳动，将每周 3-4 小时的运价情报工作压缩为 10-20 分钟的复跑流程。

## 核心数字速查（最新周：2026-05-22）

| 指标 | 数值 | 单位 | 环比 | Z分数 | 预警 |
|---|---:|---|---:|---:|---|
| 欧洲航线 | 1905.0 | USD/TEU | 4.9% | 2.76 | 红色预警 |
| 地中海航线 | 3207.0 | USD/TEU | 1.97% | 2.22 | 红色预警 |
| 美西航线 | 3154.0 | USD/FEU | 1.15% | 2.27 | 红色预警 |
| 美东航线 | 4313.0 | USD/FEU | 2.11% | 2.36 | 红色预警 |
| SCFI综合指数 | 2218.15 | points | 3.62% | 2.23 | 红色预警 |

> 数字来源：`03-analysis/CR-04A_指标计算结果.xlsx`，并在 `04-decision-report/CR-04B_业务决策建议.md`、`04-decision-report/CR-05_分析报告.md` 中复用。

## 建议阅读顺序

1. `08-submission/CR-11_作品说明文档.md`：评审入口，说明项目目标、闭环、价值和限制。
2. `03-analysis/CR-04A_指标计算结果.xlsx`：唯一指标数字源，包含最新周摘要、质量等级和公式审计示例。
3. `04-decision-report/CR-04B_业务决策建议.md`：业务决策建议，包含差异化航线建议、成本场景建议和公告措辞限制。
4. `04-decision-report/CR-05_分析报告.md`：周度分析报告，解释指标、事件关联、成本测算和数据质量限制。
5. `05-presentation/` 与 `06-visual-demo/demo-screenshots/`：展示材料、HTML占位与Demo截图。
6. `03-analysis/rerun-simulations/week2-prime/`、`03-analysis/rerun-simulations/week3-prime/`：模拟复跑证据，展示输入变化后输出变化。

## 提交包位置

- 提交目录：`08-submission/`
- 当前提交包清单：`08-submission/final-package/manifest.csv`
- 最终版材料目录：`08-submission/CR-10C_材料目录.md`

## 数据质量声明

本项目明确区分真实数据、公开线索、演示补全和待复核材料：

| 等级 | 含义 | 示例 |
|---|---|---|
| A_official | 官方或结构化可信来源 | SCFI 指标结果中的官方口径数据 |
| B_public_excerpt | 公开网页/公告摘录 | 船公司官网公告、公开线索 |
| B_screenshot_ocr | 截图OCR或人工录入复核数据 | SAFE汇率截图OCR |
| C_market_reference | 市场参考或场景化附加费 | 附加费模型输入 |
| C_demo_simulated | 演示补全或模拟复跑数据 | 缺失周补全、Week2’/Week3’复跑输入 |
| PENDING_REVIEW | 待人工复核 | 尚未形成A/B/C确定等级的线索 |

含 `C_demo_simulated`、`C_market_reference` 或 `PENDING_REVIEW` 的材料仅用于流程验证、场景演示和方法说明，不作为正式报价、审计或经营承诺口径。

## 当前仓库状态

- 当前 Git 跟踪文件：188 个。
- 评审核心材料：以 `CR-11 → CR-04A → CR-04B.md → CR-05.md → CR-09 → CR-10C` 为主线。
- 已排除内容：草稿、日志、缓存、压缩包和临时抓取页不纳入评审主仓库。
