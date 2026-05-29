# 复跑记录 Week 2'

> 记录类型：模拟真实复跑（`C_demo_simulated`）。  
> 目的：验证系统面对新增周数据、汇率和公告输入变化时，输出指标、预警与建议会同步变化；本记录不冒充正式真实行情。

## 1. 输入文件清单

- `01-raw-data/freight-index/week2-input/scfi-week2-simulated-input.csv`
- `01-raw-data/exchange-rate/week2-input/usd-cny-week2-simulated-input.csv`
- `01-raw-data/carrier-announcements/week2-input/carrier-announcement-week2-simulated.csv`
- `03-analysis/CR-04A_指标计算结果.xlsx（作为上期状态）`


## 2. 与 Week 1 相比的输入变化

- 新增周次：2026-05-29。
- SCFI综合指数：2280.0。
- 欧洲航线：1960.0 USD/TEU。
- 地中海航线：3260.0 USD/TEU。
- 美西航线：3220.0 USD/FEU。
- 美东航线：4420.0 USD/FEU。
- USD/CNY：6.8373。
- 新增公告线索：MSC 宣布 2026-06-01 起美西航线 PSS 上调 200 USD/FEU。

## 3. 运行信息

- 运行方式：读取上期状态 + 新增模拟输入 → 重算 CR-04A 指标表 → 更新最新周摘要。
- 运行耗时：0.029 秒。
- 数据等级：新增输入统一标记为 `C_demo_simulated`。

## 4. 输出文件清单

- `03-analysis/rerun-simulations/week2-prime/CR-04A_指标计算结果_week2-prime.xlsx`
- `03-analysis/rerun-simulations/week2-prime/latest-summary-week2-prime.csv`

## 5. 与 Week 1 相比的输出变化摘要

- 欧洲航线：1905.00 → 1960.00（变化 +55.00，周环比 2.89%）；预警：P95高位;Z≥2异常;连续上涨≥5周。
- 地中海航线：3207.00 → 3260.00（变化 +53.00，周环比 1.65%）；预警：P95高位;Z≥2异常;连续上涨≥5周。
- 美西航线：3154.00 → 3220.00（变化 +66.00，周环比 2.09%）；预警：P95高位;Z≥2异常;连续上涨≥5周。
- 美东航线：4313.00 → 4420.00（变化 +107.00，周环比 2.48%）；预警：P95高位;Z≥2异常;连续上涨≥5周。
- SCFI综合指数：2218.15 → 2280.00（变化 +61.85，周环比 2.79%）；预警：P95高位;Z≥2异常;连续上涨≥5周。

## 6. QA结论

- 输入文件与上期不同：通过。
- 输出关键数字与上期不同：通过。
- 模拟数据未冒充 A/B 真实数据：通过。
- 公告只作为关联线索，不作确定因果判断：通过。
