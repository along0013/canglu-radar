# 复跑记录 Week 3'

> 记录类型：模拟真实复跑（`C_demo_simulated`）。  
> 目的：验证系统面对新增周数据、汇率和公告输入变化时，输出指标、预警与建议会同步变化；本记录不冒充正式真实行情。

## 1. 输入文件清单

- `01-raw-data/freight-index/week3-input/scfi-week3-simulated-input.csv`
- `01-raw-data/exchange-rate/week3-input/usd-cny-week3-simulated-input.csv`
- `01-raw-data/carrier-announcements/week3-input/carrier-announcement-week3-simulated.csv`
- `03-analysis/rerun-simulations/week2-prime/CR-04A_指标计算结果_week2-prime.xlsx（作为上期状态）`


## 2. 与 Week 2' 相比的输入变化

- 新增周次：2026-06-05。
- SCFI综合指数：2150.0。
- 欧洲航线：1850.0 USD/TEU。
- 地中海航线：3050.0 USD/TEU。
- 美西航线：3100.0 USD/FEU。
- 美东航线：4200.0 USD/FEU。
- USD/CNY：6.85。
- 新增公告线索：Maersk 宣布美东航线临时加开一班。

## 3. 运行信息

- 运行方式：读取上期状态 + 新增模拟输入 → 重算 CR-04A 指标表 → 更新最新周摘要。
- 运行耗时：0.031 秒。
- 数据等级：新增输入统一标记为 `C_demo_simulated`。

## 4. 输出文件清单

- `03-analysis/rerun-simulations/week3-prime/CR-04A_指标计算结果_week3-prime.xlsx`
- `03-analysis/rerun-simulations/week3-prime/latest-summary-week3-prime.csv`

## 5. 与 Week 2' 相比的输出变化摘要

- 欧洲航线：1960.00 → 1850.00（变化 -110.00，周环比 -5.61%）；预警：P85偏高;周环比下跌≥5%。
- 地中海航线：3260.00 → 3050.00（变化 -210.00，周环比 -6.44%）；预警：周环比下跌≥5%。
- 美西航线：3220.00 → 3100.00（变化 -120.00，周环比 -3.73%）；预警：P85偏高。
- 美东航线：4420.00 → 4200.00（变化 -220.00，周环比 -4.98%）；预警：P85偏高。
- SCFI综合指数：2280.00 → 2150.00（变化 -130.00，周环比 -5.70%）；预警：P85偏高;周环比下跌≥5%。

## 6. QA结论

- 输入文件与上期不同：通过。
- 输出关键数字与上期不同：通过。
- 模拟数据未冒充 A/B 真实数据：通过。
- 公告只作为关联线索，不作确定因果判断：通过。
