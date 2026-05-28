# 舱路雷达｜附加费场景化模型修正记录

## 1. 修正结论

已将旧版“附加费简单求和”修正为“场景化附加费规则模型”。旧版 `canglu-demo-cost-model.csv` 仅保留作历史参考，不建议继续用于产品演示。

## 2. 新场景结果

```text
     scenario_code scenario_name_cn route_group  surcharge_usd_per_feu  applied_fee_count
         BASE_USEC           美东基础场景        USEC                  836.5                  6
         BASE_USWC           美西基础场景        USWC                  836.5                  6
       STRESS_USEC           美东压力场景        USEC                 2111.5                 11
       STRESS_USWC           美西压力场景        USWC                 2111.5                 11
USEC_PANAMA_STRESS        美东巴拿马压力场景        USEC                 2386.5                 12
```

## 3. 期末周成本测算

```text
     scenario_code scenario_name_cn  base_freight_usd_per_feu  surcharge_usd_per_feu  total_cost_usd_per_feu  fx_rate_demo  total_cost_cny_per_feu
         BASE_USEC           美东基础场景                    4313.0                  836.5                  5149.5        6.8373                35208.68
         BASE_USWC           美西基础场景                    3154.0                  836.5                  3990.5        6.8373                27284.25
       STRESS_USEC           美东压力场景                    4313.0                 2111.5                  6424.5        6.8373                43926.23
       STRESS_USWC           美西压力场景                    3154.0                 2111.5                  5265.5        6.8373                36001.80
USEC_PANAMA_STRESS        美东巴拿马压力场景                    4313.0                 2386.5                  6699.5        6.8373                45806.49
```

## 4. 文件位置

### 项目目录

- `canglu-radar/02-processed-data/surcharge-scenario-rules-2026-05.csv`
- `canglu-radar/02-processed-data/surcharge-scenario-definitions-2026-05.csv`
- `canglu-radar/02-processed-data/surcharge-scenario-calculation-detail-2026-05.csv`
- `canglu-radar/02-processed-data/surcharge-scenario-summary-2026-05.csv`
- `canglu-radar/02-processed-data/canglu-demo-cost-model-scenario-based.csv`
- `canglu-radar/02-processed-data/canglu-demo-cost-model-scenario-based.xlsx`
- `canglu-radar/02-governance/surcharge-scenario-cost-model.md`

### output 快速查看副本

- `output/surcharge-scenario-rules-2026-05.csv`
- `output/surcharge-scenario-summary-2026-05.csv`
- `output/canglu-demo-cost-model-scenario-based.csv`
- `output/canglu-demo-cost-model-scenario-based.xlsx`
- `output/surcharge-scenario-cost-model.md`

## 5. 治理口径

- 来源仍为 `C_market_reference`。
- 可用于产品Demo、成本敏感性分析、内部方案推演。
- 不可作为正式真实费率、正式报价或可审计成本依据。
- LSS 默认视为已包含于 BAF，不重复叠加。
- GRI 默认视为费率调整机制，不作为独立附加费叠加。
