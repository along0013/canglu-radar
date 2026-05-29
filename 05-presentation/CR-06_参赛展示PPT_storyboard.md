# CR-06 舱路雷达参赛展示PPT Storyboard

> 口径：本稿为正式PPT内容脚本；P6-P8数字统一来自 `03-analysis/CR-04A_指标计算结果.xlsx` 与 `04-decision-report/CR-04B_业务决策建议.docx`。  
> 数据质量：A/B/C/PENDING分层显示；C_demo_interpolation仅用于闭环演示。

## P1 封面｜舱路雷达：面向货代/外贸的航运成本与风险雷达
- 一句话：用分层数据治理 + 指标预警 + 场景化成本测算，把“看指数、查公告、算报价、写建议”的人工流程压缩为可复跑工作流。
- 关键词：真实问题、闭环验证、可复跑、多工具协同。

## P2 业务痛点｜人工看价慢、口径散、决策难复盘
- 运价指数、汇率、船司公告、附加费分散在不同来源。
- 人工周度整理耗时声称：180-240分钟；目标流程：10-20分钟（CR-09待人工复核）。
- 风险：简单看涨跌，缺少分位、Z分数、连续上涨、成本场景联动。

## P3 解决方案｜四层闭环
1. 数据层：SCFI、汇率、船司公告、附加费参考。
2. 治理层：A/B/C/PENDING分层；C级不冒充真实。
3. 分析层：分位、环比、Z分数、连续上涨、事件线索。
4. 决策层：发货/锁价/报价建议 + 场景化成本测算。

## P4 工作流｜每周替换数据即可复跑
- 输入：CSV/Excel/公告表/附加费规则。
- 处理：清洗、补全、指标计算、规则打标、报告生成。
- 输出：CR-04A、CR-04B、CR-05、PPT页、Demo脚本、QA记录。
- 当前证据：已生成3次dry-run复跑记录；外部截图补采仍PENDING。

## P5 数据治理｜专业可信而非“伪真实”
- A_official：官方/API级数据，当前不强行伪造。
- B_public_excerpt：公开页面摘录或可复核线索。
- C_chart_reference / C_demo_interpolation：图表推导或演示补全。
- PENDING：待人工补采/复核。

## P6 指标表｜最新周异常预警

route_name   value    unit     p85     p95  wow_pct  z_score  up_streak_weeks warning_level quality_level
      欧洲航线 1905.00 USD/TEU 1648.44 1784.50     4.90     2.76                4          红色预警    A_official
     地中海航线 3207.00 USD/TEU 2891.35 3144.50     1.97     2.22                4          红色预警    A_official
      美西航线 3154.00 USD/FEU 2635.50 3045.00     1.15     2.27                4          红色预警    A_official
      美东航线 4313.00 USD/FEU 3610.75 4121.00     2.11     2.36                4          红色预警    A_official
  SCFI综合指数 2218.15  points 1895.93 2094.05     3.62     2.23                4          红色预警    A_official

## P7 事件关联｜只写线索，不写因果
- 公告事件聚合表来自船司公告自然周事件表。
- 当前判断口径：高置信关联线索 / 中等关联线索；禁用确定因果词。

effective_week_start  event_count   carriers event_types association_judgement
          2025-06-09            1     Maersk         PSS  中等关联线索（仅同期观察，不作因果判断）
          2026-05-18            1     Maersk         PSS  中等关联线索（仅同期观察，不作因果判断）
          2026-06-01            2 MSC;Maersk FAK/GRI;PSS  中等关联线索（仅同期观察，不作因果判断）

## P8 成本测算与决策建议｜场景化而非简单求和

     scenario_code scenario_name_cn route_group  base_freight_usd_per_feu  surcharge_usd_per_feu  total_cost_usd_per_feu  fx_rate_demo  total_cost_cny_per_feu
         BASE_USWC           美西基础场景        USWC                    3154.0                  836.5                  3990.5        6.8373                27284.25
         BASE_USEC           美东基础场景        USEC                    4313.0                  836.5                  5149.5        6.8373                35208.68
       STRESS_USWC           美西压力场景        USWC                    3154.0                 2111.5                  5265.5        6.8373                36001.80
       STRESS_USEC           美东压力场景        USEC                    4313.0                 2111.5                  6424.5        6.8373                43926.23
USEC_PANAMA_STRESS        美东巴拿马压力场景        USEC                    4313.0                 2386.5                  6699.5        6.8373                45806.49

- 基础场景：常规报价参考。
- 压力场景：旺季/拥堵/缺箱/风险区域时使用。
- 美东巴拿马压力场景：仅适用于对应路径，不泛化。

### 最新业务建议
route_name warning_level        warning_tags                 decision_suggestion quality_level
      欧洲航线          红色预警 P95高位;Z≥2异常;连续上涨≥3周 暂停非紧急出运或拆分批次；优先锁定短期有效报价；对客户报价加入风险缓冲    A_official
     地中海航线          红色预警 P95高位;Z≥2异常;连续上涨≥3周 暂停非紧急出运或拆分批次；优先锁定短期有效报价；对客户报价加入风险缓冲    A_official
      美西航线          红色预警 P95高位;Z≥2异常;连续上涨≥3周 暂停非紧急出运或拆分批次；优先锁定短期有效报价；对客户报价加入风险缓冲    A_official
      美东航线          红色预警 P95高位;Z≥2异常;连续上涨≥3周 暂停非紧急出运或拆分批次；优先锁定短期有效报价；对客户报价加入风险缓冲    A_official


## 正式展示源文件

- HTML-first源文件：`05-presentation/cr-06-submission-deck.html`
- PPTX导出：待使用PPT专用导出流程完成；如环境不支持，HTML源文件作为可审查展示稿。
