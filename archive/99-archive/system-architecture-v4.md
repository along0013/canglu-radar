# 舱路雷达 · 系统架构 v4

> 版本 v4.0 | 2026-06-30 | 重建自 v3 设计讨论 + 全部已落盘项目文件
> 前身 v1-v3 只存在于会话摘要中，从未 write_file。v4 为首次完整落盘。

---

## 一、系统定位

舱路雷达是一个**跨境物流异常预警与发货决策情报系统**。目标：把物流专员每周 3-4h 运价情报工作压缩到 10-20min 自动复跑流程。

```
人工流程：查网页 → 算 Excel → 凭经验判断 → 写建议 → 做汇报
舱路雷达：读结构化数据 → 自动计算指标 → 规则映射建议 → 输出报告
```

---

## 二、数据管线（10 层）

```
01-raw-data/        原始数据采集（SCFI/CCFI/汇率/公告/附加费/油价/航线字典）
    │
02-governance/      数据治理（字段字典/清洗规则/质量分级定义）
02-processed-data/  清洗输出（统一格式/质量标记）
    │
03-analysis/        指标计算（P95/环比/Z分数/连续上涨/预警标签）
    │
04-decision-report/ 决策映射（按航线差异化建议/成本场景/分析报告）
    │
05-presentation/    展示层（PPT storyboard/HTML deck/可打印稿）
06-visual-demo/     视觉层（长图/Demo脚本/截图素材）
    │
07-validation/      验证层（量化对比/人工基线/复跑记录）
    │
08-submission/      提交层（评委指南/复跑说明/材料清单/ZIP打包）
    │
09-logs/            日志层（复跑记录/数据源日志）
00-control/         控制层（批次地图/命名规范/QA检查单/依赖停止清单）
```

### 核心数据链路（每周复跑）

```
原始数据CSV → 02清洗 → 03计算 → 04建议 → 05/06展示 → 07验证 → 08提交
                                                    ↑
                                          Week1/Week2/Week3 复跑验证
```

---

## 三、算法设计

### 3.1 核心指标

| 指标 | 公式 | 用途 |
|:---|:---|:---|
| P95 分位 | 26 周窗口，不排除 PENDING | 判断是否进入历史极值区间 |
| Z 分数 | `(当前值 - 26周均值) / 26周标准差` | 判断偏离程度 |
| 周环比 (WoW) | `(本周 - 上周) / 上周 × 100` | 短期变化方向 |
| 连续上涨 | 最新周往前数，直到下跌（PENDING ≠ 下跌） | 趋势持续性 |
| 预警标签 | P95高位 / Z≥2异常 / 连续上涨≥3周 / 周涨跌幅≥5% | 多维度组合 |

### 3.2 警告等级判定

```
IF Z ≥ 2.0 AND 连涨 ≥ 3 AND 当前值 ≥ P95 → 🔴 红色预警
ELIF Z ≥ 1.5 OR 当前值 ≥ P85           → 🟡 黄色预警
ELSE                                    → 🟢 绿色正常
```

### 3.3 成本场景算法（对标 Freightos 方法论）

采用 **median 区间非加权均值** —— 不定单一加权平均，展示 min/median/max：

```
场景成本 = (基础运价 + 场景附加费) / 汇率
```

5 个场景：
| 场景 | 附加费 | 适用 |
|:---|:---|:---|
| BASE_USWC | 836.5 | 美西常规报价 |
| BASE_USEC | 836.5 | 美东常规报价 |
| STRESS_USWC | 2111.5 | 旺季/拥堵/缺箱 |
| STRESS_USEC | 2111.5 | 旺季/拥堵/缺箱 |
| USEC_PANAMA_STRESS | 2386.5 | 巴拿马路径高成本 |

敏感性三维分析：汇率 (±3%) / 附加费 (基础→压力→极端) / 运价涨幅 (0→+30%)

### 3.4 报价合理性算法（对标行业方法论）

```
报价合理性区间 = [P25, P75] 窗口内各航线近26周运价
异常判定 = 当前值 ∉ 区间 → 标记为「需人工复核」
交叉验证 = SCFI(即期) / CCFI(结算) / WCI(国际) 三指数方向一致性
```

> **用户标准**：前端展示可简化，后端算法必须真实能跑。L1-L4 真做，L5-L6 标注「完整版支持」。
> 不可用"简单加权平均"冒充真实模型。

---

## 四、数据质量体系（A/B/C/PENDING）

| 等级 | 含义 | 使用边界 | 占比（26 周表） |
|:---|:---|:---|---:|
| **A_official** | 官方或可信来源 | 核心指标数字源 | 5/130 (3.8%) |
| **B_public_excerpt** | 公开网页摘录/OCR | 关联线索，保留措辞限制 | 70/130 (53.8%) |
| **C_market_reference** | 市场参考/模拟数据 | 仅演示测算和流程验证 | 0/130 |
| **PENDING** | 待补充/待复核 | 不作为结论依据 | 55/130 (42.3%) |

### 质量加权策略

```
P95 计算：仅用 A+B 级数据点；PENDING 周不参与统计但保留占位
Z 分数：同样仅 A+B；PENDING 周不参与均值/标准差计算
决策置信度：全 A → 高置信；含 B → 标注「部分数据为公开摘录」
```

---

## 五、多指数策略

### 5.1 免费指数（已采集）

| 指数 | 来源 | 最新值 | 质量 | 频率 |
|:---|:---|:---|---:|:---|
| SCFI | 上海航交所 sse.net.cn | 2985.22 | B/A | 周度 |
| CCFI | 上海航交所 sse.net.cn | 1317.36 | A | 周度 |
| SCFIS | 上海航交所 | 1863.74 | A | 周度 |
| FBX | Freightos | — | PENDING | 日度 |
| WCI | Drewry | — | PENDING | 周度 |

### 5.2 付费灰卡

| 指数 | 来源 | 状态 |
|:---|:---|---:|
| XSI-C | Xeneta | PENDING — 完整版支持 L5-L6 |

### 5.3 交叉验证逻辑

```
IF SCFI↑ AND CCFI↑ → 即期和结算同向，高置信上涨
IF SCFI↑ AND CCFI↓ → 方向背离，需复核
IF WCI↑ AND SCFI↑ → 国际和国内同向，宏观驱动
```

> Demo 阶段 SCFI + CCFI 够用；WCI/FBX/BDI 占位，标注「完整版支持 L5-L6」。

---

## 六、Hermes ↔ 小浣熊 双引擎架构

### 6.1 角色分工

| 能力 | Hermes | 办公小浣熊 |
|:---|:---:|:---:|
| 数据采集 (WebBridge) | ✅ | ❌ |
| 架构设计 + 多模型审查 | ✅ | ❌ |
| 四方会审 (Kimi/Qwen/Pro) | ✅ | ❌ |
| 纯计算 (P95/Z/场景表) | ⚠️ 可以但不应 | ✅ 三锁调教 |
| CSV ↔ JSON 格式化 | ⚠️ 可以但不应 | ✅ |
| 前端 Dashboard | ✅ | ⚠️ |
| 飞书通知 | ✅ | ✅ |

### 6.2 协作模式（文件系统中转）

```
~/小浣熊/shared/              ~/小浣熊/outputs/
    │                              ▲
    │ Hermes 写任务+数据           │ 小浣熊 写输出
    ▼                              │
┌─────────┐  Prompt+CSV  ┌──────────┐
│ Hermes  │ ──────────→  │ 办公小浣熊 │
│ (终端)  │ ←─────────── │ (桌面端)  │
└─────────┘  读取审查     └──────────┘
```

- **小浣熊无对外 API**，走文件系统是唯一稳定路径
- **三锁调教**：角色锁（只做计算）+ 格式锁（严格 CSV）+ 反幻觉锁（不准写因果词）
- **5 个预置 Prompt** 在 `~/小浣熊/shared/prompts/`

### 6.3 当前管线阶段（Day 0 → Day 4）

```
Day 0: 校验层    → validate.py（字段/值域/引用检查）
Day 1: 数据 JSON  → 5 个 JSON（metrics/history/scenarios/decisions/indices）
Day 2: HTML 骨架  → 深色航运科技风，7 区块
Day 3: JS 交互    → Chart.js + 动态渲染
Day 4: 动画+响应式 → 打磨交付
```

---

## 七、Dashboard 架构（7 区块）

纯静态 HTML + 预置 JSON，零后端，零数据库。

| 区块 | 数据源 | 可视化 |
|:---|:---|:---|
| ① 核心指标卡 | metrics.json | 4 航线 + 综合数字卡（含 Z/环比/标签） |
| ② 历史走势图 | history.json | Chart.js 折线图 × 5 航线 + P95 参考线 |
| ③ 成本场景对比 | scenarios.json | 柱状对比 + CNY/USD 双轴 |
| ④ 决策建议 | decisions.json | 卡片式展示，红/黄/绿视觉 |
| ⑤ 指数交叉验证 | indices.json | 雷达图/矩阵（PENDING 项灰色） |
| ⑥ 时效表现 | metrics.json | 效率提升 9-24x 量化 |
| ⑦ 风险雷达图 | metrics.json | 五维雷达（航线×预警等级） |

**配色**：`#0B1020` 底 + `#F9C74F` 金 + 毛玻璃卡片 + `#FF6384/#36A2EB/#FFCE56/#4BC0C0/#9966FF`

---

## 八、当前状态与缺口

### 8.1 已就绪

- ✅ 10 层管线结构完整
- ✅ 12 批次提交材料（CR-01 → CR-11 + final-package）
- ✅ A/B/C/PENDING 质量体系
- ✅ 算法设计（P95/Z/环比/连涨/median 区间/敏感性分析）
- ✅ 3 次复跑验证（Week1/Week2'/Week3'）
- ✅ 差异化航线建议（4 航线 + 综合）
- ✅ 量化验证表 + 人工 vs 自动化对比
- ✅ Hermes-小浣熊 双引擎分工方案
- ✅ 5 个预置 Prompt（`~/小浣熊/shared/prompts/`）
- ✅ 9 个输入文件（`~/小浣熊/shared/`）
- ✅ `~/小浣熊/shared/TASK.md` 小浣熊执行任务书

### 8.2 待补

| 缺口 | 优先 | 负责人 |
|:---|:---:|:---|
| 数据管线：全量 26 周 + 质量标签 + 多指数的输入 CSV 重建 | 🔴 P0 | Hermes |
| 数据管线：布伦特原油 CSV 未读入 | 🟡 P1 | Hermes |
| 数据管线：SCFIS/CCFI 历史数据未进入管线 | 🟡 P1 | Hermes |
| Day 0: validate.py 校验脚本 | 🔴 P0 | Hermes |
| Day 1-4: 小浣熊 Pipeline 执行（5 个 Prompt → 6 个输出） | 🔴 P0 | 用户→小浣熊 |
| Day 2: HTML Dashboard | 🟡 P1 | Hermes (Codex) |
| 多指数: WCI/FBX/BDI 占位 → 真实数据 | 🟠 P2 | 付费墙限制 |
| PPTX 正式导出 | 🟠 P2 | 环境依赖 |
| Demo 视频成片 | 🟠 P2 | 需录制 |

---

## 九、下一步执行序列

```
1. 四方会审本架构文档（Kimi + Qwen + Pro）—— 本会话完成
2. Hermes 重建全量数据 CSV（26周 + 多指数 + 质量标签）—— 输入小浣熊
3. 用户在小浣熊执行 TASK.md → 6 个输出文件
4. Hermes 审查 outputs/ + 修正
5. Hermes (Codex) 写 HTML Dashboard
6. Day 0 validate.py
7. 端到端集成验证
```

---

## 附录 A：数据源 URL

| 指数 | 来源 |
|:---|:---|
| SCFI | https://www.sse.net.cn/index/singleIndex?indexType=scfi |
| CCFI | https://www.sse.net.cn/index/singleIndex?indexType=ccfi |
| WCI | https://www.drewry.co.uk/supply-chain-advisors/supply-chain-expertise/world-container-index |
| FBX | https://freightos.com/freight-resources/freightos-baltic-index/ |
| BDI | https://www.balticexchange.com/en/data-services/market-information/indices.html |

## 附录 B：关键文件索引

| 文件 | 路径 |
|:---|:---|
| 本架构文档 | `plans/system-architecture-v4.md` |
| 作品说明 | `08-submission/CR-11_作品说明文档.md` |
| 指标源头 | `03-analysis/CR-04A_指标计算结果.xlsx` |
| 决策建议 | `04-decision-report/CR-04B_业务决策建议.md` |
| 敏感性分析 | `03-analysis/CR-04C_敏感性分析表.md` |
| 成本模型 | `02-governance/surcharge-scenario-cost-model.md` |
| 质量检查 | `00-control/qa-checklist.md` |
| 26 周长表 | `01-raw-data/freight-index/原始_航运指数_26周完整占位长表.csv` |
| 小浣熊任务书 | `~/小浣熊/shared/TASK.md` |
