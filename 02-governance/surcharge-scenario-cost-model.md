# 舱路雷达｜场景化附加费成本模型说明（2026-05参考行情）

## 1. 修正背景

上一版 `canglu-demo-cost-model.csv` 将可进入演示模型的附加费做了简单求和，仅可作为粗糙占位。本次已改为场景化规则模型：按费用性质、计费单位、适用航线、触发条件和叠加规则分别判断是否纳入。

## 2. 数据层级

- 附加费来源层级：`C_market_reference`
- 使用范围：仅用于演示成本测算和敏感性分析
- 不可用途：不得作为A/B层真实费率、正式报价或可审计成本依据

## 3. 默认场景

| 场景 | 说明 |
|---|---|
| BASE_USWC | 美西基础场景：基础常见费用，不启用条件性风险项 |
| BASE_USEC | 美东基础场景：基础常见费用，不启用条件性风险项 |
| STRESS_USWC | 美西压力场景：基础费用 + 旺季/拥堵/紧急燃油/缺箱/战争风险 |
| STRESS_USEC | 美东压力场景：基础费用 + 旺季/拥堵/紧急燃油/缺箱/战争风险 |
| USEC_PANAMA_STRESS | 美东经巴拿马压力场景：压力场景 + 巴拿马运河附加费 |

## 4. 场景附加费汇总

     scenario_code scenario_name_cn route_group  surcharge_usd_per_feu  applied_fee_count
         BASE_USEC           美东基础场景        USEC                  836.5                  6
         BASE_USWC           美西基础场景        USWC                  836.5                  6
       STRESS_USEC           美东压力场景        USEC                 2111.5                 11
       STRESS_USWC           美西压力场景        USWC                 2111.5                 11
USEC_PANAMA_STRESS        美东巴拿马压力场景        USEC                 2386.5                 12

## 5. 费用处理规则摘要

- BAF、THC、DOC、SEAL、AMS/ENS、设备交接单费：纳入基础场景。
- PSS、港口拥堵、EBS、CIC、WRS：仅在压力场景或对应触发条件为真时纳入。
- PCS：仅在美东且 `panama_path_flag=true` 的巴拿马路径场景纳入。
- LSS：标记为 `included_in_BAF`，默认不重复叠加。
- GRI：视为费率调整/涨价机制，可能已反映在基础运价或指数中，默认不作为附加费叠加。

## 6. 期末周测算结果

     scenario_code scenario_name_cn  base_freight_usd_per_feu  surcharge_usd_per_feu  total_cost_usd_per_feu  fx_rate_demo  total_cost_cny_per_feu
         BASE_USEC           美东基础场景                    4313.0                  836.5                  5149.5        6.8373                35208.68
         BASE_USWC           美西基础场景                    3154.0                  836.5                  3990.5        6.8373                27284.25
       STRESS_USEC           美东压力场景                    4313.0                 2111.5                  6424.5        6.8373                43926.23
       STRESS_USWC           美西压力场景                    3154.0                 2111.5                  5265.5        6.8373                36001.80
USEC_PANAMA_STRESS        美东巴拿马压力场景                    4313.0                 2386.5                  6699.5        6.8373                45806.49

## 7. 输出文件

- `02-processed-data/surcharge-scenario-rules-2026-05.csv`
- `02-processed-data/surcharge-scenario-definitions-2026-05.csv`
- `02-processed-data/surcharge-scenario-calculation-detail-2026-05.csv`
- `02-processed-data/surcharge-scenario-summary-2026-05.csv`
- `02-processed-data/canglu-demo-cost-model-scenario-based.csv`

## 8. 后续改进

后续如要进入正式报价或客户使用，需要增加船司、起运港/目的港、箱型、票数、箱量、生效日期、贸易条款和正式费率来源凭证。
