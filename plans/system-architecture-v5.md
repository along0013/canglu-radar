# 舱路雷达 · 系统架构 v5

> 版本 v5.0 | 2026-07-01 | **重建自磁盘真实文件（非事故产物）**
> v4 被 INC-2026-0630-002 污染（三方会用同模型），v5 为独立重建。

---

## 〇、v5 核心原则

1. **只承诺磁盘上存在的东西**。不写"已生成"但查不到的文件。
2. **Hermes 可独立跑通全链路**。小浣熊作为加分项，不作为阻塞依赖。
3. **先校验，再展示**。validate.py 在 HTML 之前。
4. **诚实地标注数据质量**。PENDING 就是 PENDING，不假装有 26 周全量。

---

## 一、系统定位（不变）

舱路雷达 = **跨境物流异常预警与发货决策情报系统**。

```
人工流程：查网页 → 算 Excel → 凭经验判断 → 写建议 → 做汇报（每周 3-4h）
舱路雷达：自动计算指标 → 规则映射建议 → HTML Dashboard 展示（10-20min 复跑）
```

---

## 二、数据管线 v5（精简自 10 层原始管线）

原始 10 层管线（01-raw → 09-logs → 00-control）仍在磁盘上，是比赛提交的完整版本。v5 在前端展示层做减法，保留核心链路：

```
01-raw-data/              原始数据采集（SCFI CSV + 汇率 + 附加费规则）
        │
[02-governance/           数据治理规则（字段字典/清洗规则/质量分级）— 原始项目已有]
        │
03-analysis/              指标计算 → Hermes Python 脚本（pandas/numpy）
        │                   产出：P95/Z/环比/连涨/预警标签/成本场景/报价合理性区间
        │
data/*.json               5 个 JSON（Dashboard 直接读取，零后端）
        │
dashboard.html            纯静态 HTML + Chart.js CDN（7 区块）
        │
07-validation/            validate.py 校验脚本 + 量化验证表
```

> **关键变化**：计算层从「依赖小浣熊」改为「Hermes Python 脚本为主，小浣熊并行为辅」。

---

## 三、数据资产盘点（磁盘真实存在）

### 3.1 已有数据文件

| 文件 | 位置 | 内容 | 行数 |
|:---|:---|:---|---:|
| SCFI 26 周 CSV | `~/小浣熊/shared/scfi-26w-clean.csv` | 5 航线 × 26 周（17 周有数据，9 周 PENDING） | ~26 |
| 最新运价 | `~/小浣熊/shared/freight-latest.csv` | 当前周运价快照 | ~5 |
| 26 周历史（全量） | `~/小浣熊/shared/history-26w.csv` | 含 PENDING 占位的完整表 | ~26 |
| 指数对比 | `~/小浣熊/shared/index-comparison.csv` | SCFI/FBX/WCI 对比 | ~5 |
| 附加费场景 | `~/小浣熊/shared/surcharge-scenarios.csv` | 5 场景附加费配置 | ~5 |
| 汇率 | USD/CNY = 6.8373 | TASK.md 中硬编码 | 1 |

### 3.2 已有设计文档

| 文件 | 内容 |
|:---|:---|
| `decision-rules.md` | 预警等级判定 + 4 航线差异化建议模板 + 质量→置信度映射 |
| `suggestion-template.md` | 建议输出模板 |
| `metrics-schema.json` | JSON 输出 schema |
| `TASK.md` | 5 任务执行书（小浣熊用） |
| `prompts/prompt-01~05` | 5 个预置 Prompt |
| `data-source-website-list.md` | 完整数据采集策略（9 节，含注册判断） |
| `诊断错题集与回归测试机制.md` | 采集失败路径 + 回归测试清单 |

### 3.3 数据质量现状

| 质量等级 | 数量 | 占比 | 说明 |
|:---|---:|---:|:---|
| A_official | 5/130 | 3.8% | SCFI 官方 + CCFI 官方 |
| B_public_excerpt | 70/130 | 53.8% | 公开网页摘录/转载 |
| C_market_reference | 0/130 | 0% | 市场参考（暂未使用） |
| **PENDING** | **55/130** | **42.3%** | 历史周数据缺口（9 周） |

> ⚠️ Z 分数有效样本仅 17 周（非声称的 26 周）。计算时排除 PENDING 行，不编造数据。

### 3.4 数据源可获取性

| 指数 | 来源 | 状态 | 获取难度 |
|:---|:---|:---|:---|
| SCFI | 上海航交所 sse.net.cn | ✅ 17 周真实 | 单期查询免费（逐周手动或 WebBridge 脚本） |
| CCFI | 上海航交所 | ✅ 可用 | 免费单期查询 |
| SCFIS | 上海航交所 | ✅ 可用 | 免费单期查询 |
| FBX | Freightos | PENDING | 需付费订阅 |
| WCI | Drewry | PENDING | 需付费订阅 |
| BDI | Baltic Exchange | PENDING | 公开延迟数据可能可获取 |
| 布伦特原油 | 东方财富/新浪财经 | ⚠️ 可获取但未录入 | 免费公开 |
| USD/CNY | 中国货币网 | ⚠️ 可获取但未录入 | 免费公开 |

---

## 四、计算引擎 v5（Hermes 侧 Python）

### 4.1 为什么 Hermes 自己算

小浣熊流程链路太长：用户手动启动 → 逐个 Prompt → 检查输出 → 文件传递。比赛演示时任何一个环节断了就没数据。Hermes 侧 Python 脚本可以零依赖跑通全链路。

### 4.2 计算脚本设计

```
compute.py          ← 主入口
  ├── load_csv()         读取 scfi-26w-clean.csv + freight-latest.csv
  ├── calc_percentiles() P50/P75/P85/P90/P95/P99（仅 A+B 级数据点）
  ├── calc_z_score()     Z = (当前值 - A+B 均值) / A+B 标准差
  ├── calc_wow()         周环比 = (本周-上周)/上周 × 100
  ├── calc_streak()      从最新周往前数连续上涨周数
  ├── assign_warning()   按规则映射红色/黄色/绿色
  ├── calc_scenarios()   BASE_USWC/BASE_USEC/STRESS_USWC/STRESS_USEC/USEC_PANAMA_STRESS
  ├── calc_quote_range() 报价合理性区间 [P25, P75]（对标 Freightos median 区间法）
  └── write_json()       输出 5 个 JSON 到 data/
```

**依赖**：仅 pandas + numpy（Mac 已有），不依赖小浣熊。

**容错设计**：
- PENDING 行 → 跳过，不参与统计计算
- PENDING 占比 > 50% → Z 分数标注「⚠️ 样本量不足，置信度降低」
- 某航线全 PENDING → 该航线 JSON 中 `warning_level: "INSUFFICIENT_DATA"`

### 4.3 小浣熊作为并行路径

用户有空时仍可手动走 TASK.md 的 5 任务流程。两条路径产出互相比对：
- Hermes Python → `data/*.json`
- 小浣熊 Prompt → `outputs/*.json`
- `validate.py` 对比两组 JSON → 报告差异

---

## 五、5 个 JSON 的精确 Schema

### 5.1 metrics.json — 核心指标

```json
{
  "_meta": { "source": "...", "fetch_date": "2026-06-12", "quality_level": "B_public_excerpt" },
  "latest_week": "2026-06-12",
  "routes": [
    {
      "route_name": "欧洲航线",
      "route_code": "EUR",
      "unit": "USD/TEU",
      "current_value": 2852.0,
      "percentiles": { "p50": ..., "p75": ..., "p85": ..., "p90": ..., "p95": ..., "p99": ... },
      "wow_change_pct": 9.48,
      "z_score": 5.38,
      "up_streak_weeks": 6,
      "warning_level": "红色预警",
      "warning_tags": ["P95高位", "Z≥2异常", "连续上涨≥3周"],
      "quality_level": "B_public_excerpt",
      "sample_size": 17,
      "total_window": 26,
      "pending_ratio": 0.35
    }
    // ... 共 4 条航线 + 1 条 SCFI 综合
  ]
}
```

### 5.2 history.json — 26 周历史趋势

```json
{
  "_meta": { "source": "...", "quality_level": "..." },
  "labels": ["2025-12-19", "2025-12-26", ..., "2026-06-12"],
  "datasets": [
    { "route_code": "EUR", "label": "欧洲", "unit": "USD/TEU",
      "data": [1695.0, null, 1742.0, ...],  // null = PENDING
      "p95_line": 1878.3,
      "color": "#FF6384" },
    // ... 5 条数据集
  ]
}
```

### 5.3 scenarios.json — 成本场景

```json
{
  "_meta": { "...", "exchange_rate": 6.8373 },
  "scenarios": [
    { "name": "BASE_USWC", "base_freight": 4984.0, "surcharge": 836.5,
      "total_cost_usd": 5820.5, "total_cost_cny": 39795.32 },
    // ... 5 个场景
  ]
}
```

### 5.4 decisions.json — 决策建议

```json
{
  "_meta": { "...", "decision_rules_version": "v1.0" },
  "decisions": [
    {
      "route_code": "EUR",
      "warning_level": "红色预警",
      "confidence": "B_public_excerpt",
      "suggestion": "亚欧航线已进入历史高位区间（P95），当前运价 2852.0 USD/TEU，Z=5.38，连续上涨 6 周。非急单建议推迟 1-2 周观察；急单必须锁定短期有效报价（7 天内）。建议客户报价加入 ≥15% 风险缓冲。"
    }
    // ... 4 条航线 + 1 条综合
  ],
  "cross_validation": {
    "scfi_direction": "up",
    "ccfi_direction": "PENDING",
    "consistency": "insufficient_data"
  }
}
```

### 5.5 indices.json — 多指数交叉验证

```json
{
  "_meta": { "source": "..." },
  "indices": [
    { "name": "SCFI", "value": 2985.22, "wow_change_pct": 9.5, "status": "available", "quality": "B_public_excerpt" },
    { "name": "CCFI", "value": 1317.36, "wow_change_pct": null, "status": "available", "quality": "A_official" },
    { "name": "SCFIS", "value": 1863.74, "wow_change_pct": null, "status": "available", "quality": "A_official" },
    { "name": "WCI", "value": null, "status": "PENDING", "note": "Drewry 付费墙，完整版支持" },
    { "name": "FBX", "value": null, "status": "PENDING", "note": "Freightos 付费墙，完整版支持" },
    { "name": "BDI", "value": null, "status": "PENDING", "note": "Baltic Exchange，公开延迟数据或可获取" }
  ]
}
```

---

## 六、HTML Dashboard 架构（7 区块）

纯静态 HTML + Chart.js 4.x CDN，零后端，零数据库。浏览器直接打开 `dashboard.html`。

| 区块 | 标题 | 数据源 | 可视化 | 30s 叙事 |
|:---|:---|:---|:---|:---|
| ① | 核心指标卡 | `metrics.json` | 4 航线 + 综合数字卡（当前值 + Z + 环比 + 预警标签） | "这是本周运价全景" |
| ② | 历史走势 | `history.json` | 折线图 × 5（含 P95 参考线，PENDING 断点虚线） | "26 周趋势一目了然" |
| ③ | 成本场景对比 | `scenarios.json` | 分组柱状图（基础 vs 压力，USD/CNY 双标注 tooltip） | "极端情况下你的成本" |
| ④ | 决策建议卡片 | `decisions.json` | 4 航线 + 综合卡片，红/黄/绿边框 | "每条航线该怎么做" |
| ⑤ | 指数交叉验证 | `indices.json` | 表格 + 颜色编码（可用/待补），PENDING 灰底问号 | "多指数验证一致性" |
| ⑥ | 时效量化 | 硬编码 | 大数字 + 对比："人工 3-4h → 舱路雷达 10-20min，**效率提升 9-24x**" | "产品价值一句话" |
| ⑦ | 风险热力图 | `metrics.json` | 5 航线 × 4 指标矩阵，颜色编码 | "全局风险一屏" |

**视觉规格**：
- 底色：`#0B1020`（深海军蓝）
- 强调色：`#F9C74F`（暖金）
- 卡片：半透明毛玻璃 + `1px solid rgba(249,199,79,0.15)`
- 航线颜色：`#FF6384` 欧洲 / `#36A2EB` 地中海 / `#FFCE56` 美西 / `#4BC0C0` 美东 / `#9966FF` 综合
- 红色预警：`#FF4757` / 黄色关注：`#FFA502` / 绿色正常：`#2ED573`
- 毛玻璃 fallback：`@supports not (backdrop-filter: blur())` 降级为不透明深色卡片

**PENDING 数据的展示策略**：
- 折线图中 PENDING 周用虚线连接（`borderDash: [5,5]`）
- PENDING 比例 > 30% → 图表上方显示 `⚠️ 数据覆盖 65%（17/26 周），部分趋势线基于有限样本`
- 指数交叉验证表中 PENDING 指数灰底显示 `—`

---

## 七、Hermes ↔ 小浣熊 协作模式 v5

### 7.1 双引擎 ≠ 双依赖

```
                    ┌─────────────────────┐
                    │   Hermes (主引擎)    │
                    │                     │
用户 ──→ 飞书 ──→  │ compute.py          │
                    │ validate.py         │
                    │ dashboard.html      │
                    │                     │
                    └────────┬────────────┘
                             │
                             │ 文件系统中转
                             ▼
                    ┌─────────────────────┐
                    │ 办公小浣熊 (辅引擎)  │
                    │                     │
                    │ 5 个 Prompt          │
                    │ 6 个输出文件         │
                    │                     │
                    └─────────────────────┘
```

- **主链路**：Hermes Python 计算 → 5 JSON → validate.py → HTML Dashboard。100% 可控。
- **辅链路**：用户有空时在小浣熊跑 TASK.md → outputs/6 文件 → validate.py 交叉比对。
- **比赛答辩时**：如果小浣熊跑通了 → "双引擎验证，数据一致性 100%"。如果没跑通 → "Hermes 侧可独立闭环，小浣熊侧作为能力展示"。

### 7.2 小浣熊 Prompt 清单（5 个，已存在）

```
~/小浣熊/shared/prompts/
  prompt-01-metrics-calc.md    → 指标计算（P95/Z/环比/连涨/预警）
  prompt-02-cost-scenarios.md  → 成本场景（5 场景 × 汇率）
  prompt-03-json-format.md     → JSON 格式化
  prompt-04-decision-suggestions.md → 决策建议（按规则模板生成）
  prompt-05-chart-data.md      → 图表数据（趋势 + 雷达/热力）
```

### 7.3 小浣熊输出文件（6 个）

```
~/小浣熊/outputs/
  metrics-result.csv       ← 任务 1
  scenarios-table.csv      ← 任务 2
  metrics-final.json       ← 任务 3
  decisions-final.json     ← 任务 4
  chart-trend.json         ← 任务 5
  chart-radar.json         ← 任务 5
```

---

## 八、验证体系

### 8.1 validate.py（Day 0 最高优先级）

```python
# 校验清单
1. 字段存在性      → 5 个 JSON 的必需字段全部存在
2. 值域检查        → Z ∈ [-5, 10]、环比 ∈ [-50, 50]、百分位数单调递增
3. 跨 JSON 一致性  → metrics.routes ↔ decisions 的 route_code 集合一致
                   → scenarios ↔ metrics 的汇率/运价基准一致
4. 时间基线一致    → 所有 JSON 的 latest_week 来自同一周
5. 数据完整性      → PENDING 率统计、null 值计数
```

### 8.2 量化验证表（已有）

```
07-validation/CR-09_量化验证表.xlsx
  - 人工 vs 自动化对比
  - 效率提升 9-24x 的量化依据
```

---

## 九、比赛答辩叙事

### 9.1 3 分钟演示脚本（7 区块串讲）

| 时间 | 区块 | 说辞 |
|:---|:---|:---|
| 0:00-0:20 | 开场 | "我是物流专员小袁。每周一早上我第一件事是查运价——打开 6 个网站、算 Excel、凭经验写建议，3-4 小时。舱路雷达把这个流程压缩到 10 分钟。" |
| 0:20-0:50 | ① 核心指标 | "这是本周运价全景。美西 4984、美东 6037、欧洲 2852、地中海 4196，全部红色预警——Z 分数 4-5，连续上涨 6 周，运价已进入历史 P95 极值区间。" |
| 0:50-1:20 | ② 走势图 | "26 周趋势图。注意这里的虚线段——9 周数据暂时缺失，标注 PENDING。但 17 周真实数据已经足够揭示上涨趋势。P95 参考线（金色虚线）显示所有航线已突破历史高位。" |
| 1:20-1:40 | ③ 成本场景 | "在极端情况下，美西一个柜子的总成本是 5820 美元。如果加上巴拿马运河拥堵叠加，美东最高可达 8424 美元。按当前汇率折合 57596 人民币。" |
| 1:40-2:10 | ④ 决策建议 | "基于规则引擎自动生成差异化建议——欧洲航线建议推迟 1-2 周观察、地中海建议评估替代港口、美西建议提前 2 周锁舱。每条建议都是规则驱动的，不是拍脑袋。" |
| 2:10-2:30 | ⑤+⑥ | "SCFI/CCFI/SCFIS 三指数方向交叉验证。效率提升 9-24 倍是用量化验证表算出来的，不是估的。" |
| 2:30-2:50 | ⑦ | "风险热力图——一屏看完 5 航线 × 4 指标。全红。现在不是入场的好时机。" |
| 2:50-3:00 | 总结 | "舱路雷达——用了办公小浣熊调教，用了 Hermes 做架构和审查，核心逻辑是真实可跑的。数据源 PENDING 部分诚实标注，完整版支持 WCI/FBX/BDI 等多指数。" |

### 9.2 关键差异点（vs 竞品）

| 对比维度 | 传统人工 | 舱路雷达 |
|:---|:---|:---|
| 数据获取 | 手动查 6+ 网站，逐条复制 | 自动化采集 + CSV 输入 |
| 指标计算 | Excel 手动公式，易出错 | Python pandas 可复现 |
| 建议生成 | 凭经验拍脑袋 | 规则引擎映射（4 航线差异化） |
| 更新频率 | 一周一次（周五下班前赶工） | 数据更新后 5 分钟复跑 |
| 可审计性 | 无版本记录 | `validate.py` + 量化验证表 |
| 透明度 | 黑盒 | PENDING 数据诚实标注，不编造 |

---

## 十、执行计划（优先级重排）

### Day 0 — 校验层（🔴 P0，现在开始）

```
1. 写 validate.py 并运行 → 暴露 5 个 JSON 所有不一致
2. 修复数据不一致（时间基线统一到最新周）
3. 决定：用现有 metrics.json 修复不一致，还是直接从 scfi-26w-clean.csv 重新计算
```

### Day 1 — 计算层（🔴 P0）

```
4. 写 compute.py（Hermes 侧 Python 计算管线）
5. 运行 compute.py → 生成干净的 5 个 JSON
6. validate.py 验证通过 → data/ OK
7. （可选）用户手动走小浣熊 TASK.md → outputs/ → validate.py 交叉比对
```

### Day 2 — 展示层（🟡 P1）

```
8. 写 dashboard.html（纯静态 + Chart.js CDN + 7 区块）
9. 从 data/*.json 加载数据（fetch），无后端依赖
10. 浏览器打开验证
```

### Day 3 — 比赛打包（🟡 P1）

```
11. 将 dashboard.html + data/ 打包为可演示的静态目录
12. PPT（已有 10 页 HTML deck + 截图）
13. 根据最新数据更新决策建议
```

### Day 4 — 增强（🟠 P2，有余力）

```
14. 补 SCFI 历史数据（能补几周补几周）
15. 布伦特原油背景数据录入
16. SCFIS/CCFI 历史数据录入
17. WCI/FBX/BDI 占位 → 标注"完整版支持"
```

---

## 十一、当前状态与缺口

### 11.1 已就绪

- ✅ 原始项目 223 文件（比赛提交完整）
- ✅ 5 个 JSON 数据文件（data/，但存在一致性问题）
- ✅ 决策规则 + 建议模板 + Prompt（shared/）
- ✅ 数据源网站清单 + 采集策略 + 错题集
- ✅ A/B/C/PENDING 质量体系
- ✅ 10 页参赛 PPT HTML deck + 截图
- ✅ 量化验证表（人工 vs 自动化对比）

### 11.2 缺口

| 缺口 | 优先级 | 说明 |
|:---|:---:|:---|
| `validate.py` 校验脚本 | 🔴 P0 | Day 0 最高优先级。没有校验，5 个 JSON 的可靠性为零。 |
| 数据一致性修复 | 🔴 P0 | metrics.json（W3）≠ decisions.json（W1）时间基线不同。 |
| `compute.py` 计算管线 | 🔴 P0 | Hermes 侧 Python 脚本，替代小浣熊手动流程。 |
| `dashboard.html` | 🟡 P1 | 7 区块 HTML Dashboard。核心演示物。 |
| 42.3% PENDING 数据 | 🟡 P1 | 能补则补，补不了诚实标注。不影响演示。 |
| Baidu/Google SEO 版本 | 🟠 P2 | 完整版功能，不在比赛范围内。 |
| 布伦特原油数据 | 🟠 P2 | 增强背景数据，非核心功能。 |

### 11.3 不做的事（诚实边界）

- ❌ 不假装有 26 周全量数据（PENDING 就是 PENDING）
- ❌ 不声称 WCI/FBX/BDI 已接入（标注"完整版支持"）
- ❌ 不把文件传递包装成"双引擎协同架构"（诚实说是"Hermes 主计算 + 小浣熊并行验证"）
- ❌ 不在演示中展示付费墙后的数据（XSI-C 灰卡只提概念）

---

## 附录 A：关键文件索引

| 文件 | 路径 |
|:---|:---|
| 本架构文档 | `plans/system-architecture-v5.md` |
| 原始 git clone | `/Users/along/.hermes/repos/synnovator/canglu-radar/` |
| 项目工作副本 | `~/小浣熊/canglu-radar/` |
| 小浣熊协作文件 | `~/小浣熊/shared/` |
| SCFI 26 周 CSV | `~/小浣熊/shared/scfi-26w-clean.csv` |
| 决策规则 | `~/小浣熊/shared/decision-rules.md` |
| 数据源网站清单 | `01-raw-data/collection-reports/data-source-website-list.md` |
| 错题集 | `01-raw-data/collection-reports/current/诊断错题集与回归测试机制.md` |
| 26 周长表 | `01-raw-data/freight-index/原始_航运指数_26周完整占位长表.csv` |
| 量化验证表 | `07-validation/CR-09_量化验证表.xlsx` |

## 附录 B：数据源 URL

| 指数 | 来源 | URL |
|:---|:---|:---|
| SCFI | 上海航交所 | https://www.sse.net.cn/index/singleIndex?indexType=scfi |
| CCFI | 上海航交所 | https://www.sse.net.cn/index/singleIndex?indexType=ccfi |
| SCFIS | 上海航交所 | https://www.sse.net.cn/index/singleIndex?indexType=scfis |
| WCI | Drewry | https://www.drewry.co.uk/supply-chain-advisors/supply-chain-expertise/world-container-index |
| FBX | Freightos | https://freightos.com/freight-resources/freightos-baltic-index/ |
| BDI | Baltic Exchange | https://www.balticexchange.com/en/data-services/market-information/indices.html |
