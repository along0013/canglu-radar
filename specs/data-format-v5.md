# 舱路雷达 · 数据格式统一规范 v5.0

> 2026-07-01 | 所有 JSON/CSV 的唯一权威格式定义
> 任何计算脚本、Dashboard、validate.py 都以此文件为准

---

## 〇、航线命名（全局唯一）

```
route_code    route_name       unit          category
─────────────────────────────────────────────────────
EUR           欧洲航线          USD/TEU       集装箱即期运价
MED           地中海航线        USD/TEU       集装箱即期运价
USWC          美西航线          USD/FEU       集装箱即期运价
USEC          美东航线          USD/FEU       集装箱即期运价
COMPOSITE     SCFI综合指数      points        综合指数
```

> **全项目统一 route_code**。CSV 列名、JSON key、Dashboard 引用全部用它。

---

## 一、CSV 输入层

### 1.1 主数据表 `scfi-26w.csv`

> 这是唯一的权威数值源。所有 JSON 从这里计算得出。

```
week,COMPOSITE,USWC,USEC,EUR,MED
2025-11-28,1403.13,1632,2428,1404,2232
2025-12-05,1397.63,1550,2315,1400,2300
...
2026-06-12,2985.22,4984,6286,2852,4196
```

| 规则 | 说明 |
|:---|:---|
| 列名 | 用 route_code，不再用 `CN-` 前缀或 `CN-EUR` 式命名 |
| 空值 | 直接留空（不是 `null` 不是 `0` 不是 `PENDING`） |
| 日期 | `YYYY-MM-DD`，取当周周五 |
| 编码 | UTF-8，无 BOM |
| 数值 | 整数或保留 2 位小数，不写单位 |

### 1.2 附加费配置 `surcharge-scenarios.csv`

```
scenario_code,route_group,surcharge_usd_per_feu,applied_fee_count
BASE_USWC,USWC,836.5,6
BASE_USEC,USEC,836.5,6
STRESS_USWC,USWC,2111.5,11
STRESS_USEC,USEC,2111.5,11
USEC_PANAMA_STRESS,USEC,2386.5,12
```

> `route_group` 引用 `route_code`（USWC / USEC）。后续如果欧洲/地中海航线需要场景，扩展此文件即可。

### 1.3 指数对比 `index-comparison.csv`

```
index_code,index_name,value,unit,date,quality_level,status
SCFI,上海出口集装箱运价指数,2985.22,points,2026-06-12,B_public_excerpt,collected
CCFI,中国出口集装箱运价指数,1317.36,points,2026-05-22,A_official,collected
SCFIS,上海出口集装箱结算运价指数,1863.74,points,2026-05-22,A_official,collected
WCI,Drewry World Container Index,,USD/FEU,,PENDING,完整版支持
FBX,Freightos Baltic Index,,USD/FEU,,PENDING,完整版支持
BDI,波罗的海干散货运价指数,,points,,PENDING,完整版支持
```

> 新增 `SCFIS`（已有数据可使用）。`index_code` 统一大写。

---

## 二、JSON 输出层

### 通用 _meta / _stats

**每个 JSON 必须有这两个根字段。** `_meta` 是溯源信息，`_stats` 是数据健康度。

```json
{
  "_meta": {
    "version": "5.0",
    "latest_week": "2026-06-12",
    "generated_at": "2026-07-01T12:00:00+08:00",
    "quality_level": "B_public_excerpt",
    "source": "SCFI 上海航运交易所官网 + 公开转载数据",
    "fx_rate": 6.8373,
    "note": "17/26 周有真实数据，9 周 PENDING。Z 分数仅基于有效样本计算。"
  },
  "_stats": {
    "total_data_points": 130,
    "pending_count": 55,
    "pending_ratio": 0.423,
    "effective_sample_size": 17,
    "window_size": 26
  }
}
```

### 2.1 `metrics.json` — 核心指标

```json
{
  "_meta": { ... },
  "routes": [
    {
      "code": "EUR",
      "name": "欧洲航线",
      "unit": "USD/TEU",
      "current_value": 2852.0,
      "percentiles": {
        "p50": 1553.75,
        "p75": 1627.38,
        "p85": 1740.4,
        "p90": 1740.4,
        "p95": 1878.3,
        "p99": 2423.0
      },
      "wow_change_pct": 9.48,
      "z_score": 5.38,
      "up_streak_weeks": 6,
      "warning_level": "红色预警",
      "warning_tags": ["P95高位", "Z≥2异常", "连续上涨≥3周", "周涨跌幅≥5%"],
      "quality_level": "B_public_excerpt"
    }
    // ... 共 5 条（EUR/MED/USWC/USEC/COMPOSITE）
  ],
  "market_regime": {
    "overall_warning": "红色预警",
    "routes_in_red": 5,
    "routes_in_yellow": 0,
    "routes_in_green": 0,
    "description": "全航线进入历史极值区间，SCFI 综合指数 Z=5.38，建议全航线收紧报价有效期"
  },
  "_stats": { ... }
}
```

| 字段 | 类型 | 必填 | 说明 |
|:-----|:-----|:-----|:-----|
| `code` | string | ✅ | route_code |
| `name` | string | ✅ | 中文名 |
| `unit` | string | ✅ | USD/TEU / USD/FEU / points |
| `current_value` | number | ✅ | 最新周运价值 |
| `percentiles.pXX` | number | ✅ | P50/P75/P85/P90/P95/P99，仅 A+B 级数据计算 |
| `wow_change_pct` | number | ✅ | 周环比%，保留 2 位小数 |
| `z_score` | number | ✅ | 标准差倍数，保留 2 位小数 |
| `up_streak_weeks` | integer | ✅ | 连续上涨周数 |
| `warning_level` | enum | ✅ | 红色预警 / 黄色预警 / 绿色正常 |
| `warning_tags` | array | ✅ | P95高位/Z≥2异常/连续上涨≥3周/周涨跌幅≥5%/≥10% |
| `quality_level` | enum | ✅ | A_official/B_public_excerpt/C_market_reference/PENDING |

### 2.2 `history.json` — 26 周历史趋势

```json
{
  "_meta": { ... },
  "labels": ["2025-11-28", "2025-12-05", ..., "2026-06-12"],
  "datasets": [
    {
      "code": "EUR",
      "name": "欧洲航线",
      "unit": "USD/TEU",
      "color": "#FF6384",
      "p95_line": 1878.3,
      "data": [1404, 1400, null, 1533, 1690, null, null, ...]
    }
    // ... 共 5 条数据集
  ],
  "_stats": { ... }
}
```

| 规则 | 说明 |
|:---|:---|
| `data[]` | PENDING 周 = `null`（不写 0 或 "PENDING"） |
| `labels` | 必须和 `data[]` 一一对应，长度相等 |
| `color` | 固定调色板：EUR=#FF6384, MED=#36A2EB, USWC=#FFCE56, USEC=#4BC0C0, COMPOSITE=#9966FF |
| `p95_line` | 来自 metrics.json 同航线，用于 Chart.js 参考线 |

### 2.3 `scenarios.json` — 成本场景

```json
{
  "_meta": { ... },
  "scenarios": [
    {
      "code": "BASE_USWC",
      "name": "美西基础场景",
      "route_code": "USWC",
      "base_freight_usd": 4984.0,
      "surcharge_usd": 836.5,
      "total_cost_usd": 5820.5,
      "total_cost_cny": 39795.32,
      "description": "基础常见费用（BAF/THC/DOC/SEAL/AMS/设备交接单），不启用条件性风险项",
      "risk_level": "normal"
    },
    {
      "code": "STRESS_USWC",
      "name": "美西压力场景",
      "route_code": "USWC",
      "base_freight_usd": 4984.0,
      "surcharge_usd": 2111.5,
      "total_cost_usd": 7095.5,
      "total_cost_cny": 48513.78,
      "description": "含 PSS/GRI/BAF 上浮/拥堵附加费，共 11 项费用",
      "risk_level": "stress"
    }
    // ... 共 5 个场景
  ],
  "sensitivity": {
    "fx_rate_range": [6.6322, 6.8373, 7.0424],
    "surcharge_multipliers": [1.0, 1.5, 2.0],
    "freight_change_pct": [0, 10, 20, 30]
  },
  "_stats": { ... }
}
```

| 场景 code | route_code | 用途 |
|:---|:---|:---|
| `BASE_USWC` | USWC | 美西常规报价 |
| `STRESS_USWC` | USWC | 旺季/拥堵/缺箱 |
| `BASE_USEC` | USEC | 美东常规报价 |
| `STRESS_USEC` | USEC | 旺季/拥堵 |
| `USEC_PANAMA_STRESS` | USEC | 巴拿马路径极端场景 |

> `base_freight_usd` 必须与 `metrics.json` 同航线 `current_value` 一致（从同一周取值）。

### 2.4 `decisions.json` — 决策建议

```json
{
  "_meta": { ... },
  "decisions": [
    {
      "code": "EUR",
      "name": "欧洲航线",
      "warning_level": "红色预警",
      "suggestion": "亚欧航线已进入历史高位区间（P95），当前运价 2852.0 USD/TEU，Z=5.38，连续上涨 6 周。非急单建议推迟 1-2 周观察；急单必须锁定短期有效报价（7 天内）。建议客户报价加入 ≥15% 风险缓冲。",
      "confidence": "B_public_excerpt",
      "source_metrics": ["P95高位", "Z≥2异常", "连续上涨≥3周"]
    }
    // ... 共 5 条
  ],
  "cross_validation": {
    "scfi_direction": "up",
    "ccfi_direction": "up",
    "consistency": "consistent",
    "note": "SCFI 与 CCFI 同向上涨，高置信。缺少 WCI/FBX 三方验证。"
  },
  "_stats": { ... }
}
```

| 规则 | 说明 |
|:---|:---|
| `suggestion` | 按 `decision-rules.md` 模板填充 `{current_value}`/`{z_score}`/`{up_streak}` 等变量 |
| 禁用词 | 不得出现"导致""引起""必然""因果" |
| `confidence` | A_official → 直接建议 / B_public_excerpt → "建议""可考虑" / PENDING → ⚠️仅提示关注 |
| `cross_validation` | SCFI/CCFI/SCFIS 三者方向一致性判断 |

### 2.5 `indices.json` — 多指数交叉验证

```json
{
  "_meta": { ... },
  "indices": [
    {
      "code": "SCFI",
      "name": "上海出口集装箱运价指数",
      "value": 2985.22,
      "unit": "points",
      "date": "2026-06-12",
      "quality_level": "B_public_excerpt",
      "status": "collected",
      "source_url": "https://www.sse.net.cn/index/singleIndex?indexType=scfi"
    },
    {
      "code": "CCFI",
      "name": "中国出口集装箱运价指数",
      "value": 1317.36,
      "unit": "points",
      "date": "2026-05-22",
      "quality_level": "A_official",
      "status": "collected",
      "source_url": "https://www.sse.net.cn/index/singleIndex?indexType=ccfi"
    },
    {
      "code": "WCI",
      "name": "Drewry World Container Index",
      "value": null,
      "unit": "USD/FEU",
      "date": null,
      "quality_level": "PENDING",
      "status": "完整版支持",
      "source_url": "https://www.drewry.co.uk/..."
    }
    // ... FBX, BDI 同理
  ],
  "_stats": { ... }
}
```

> `value=null` + `status="完整版支持"` 表示 PENDING 指数占位。`date` 为 null 同样表示无数据。

---

## 三、字段命名对照（旧→新）

| 旧名（历史 JSON） | 新名（v5 统一） | 出现位置 |
|:---|:---|:---|
| `CN-USWC` / `CN-USEC` / `CN-EUR` / `CN-MED` | `USWC` / `USEC` / `EUR` / `MED` | CSV 列名 |
| `route_name ` | `name` | metrics/decisions |
| `route_code` | `code` | 全局 |
| `p95` (单独值) | `percentiles.p95` | metrics |
| `wow_pct` | `wow_change_pct` | metrics/decisions |
| `composite` (history.json) | `COMPOSITE` | 全局 |
| `europe` (history.json) | `EUR` | 全局 |
| `med` (history.json) | `MED` | 全局 |
| `uswc` (history.json) | `USWC` | 全局 |
| `usec` (history.json) | `USEC` | 全局 |
| `current_value` (indices.json) | `value` | indices |

---

## 四、值域约束

| 字段 | 范围 | 不满足时的行为 |
|:---|:---|:---|
| `z_score` | [-5.0, 10.0] | validate.py 报 WARNING，但仍保留原值 |
| `wow_change_pct` | [-50.0, 50.0] | 同上 |
| `up_streak_weeks` | [0, 26] | 超出报 ERROR |
| `percentiles` 单调性 | p50 ≤ p75 ≤ p85 ≤ p90 ≤ p95 ≤ p99 | 违反报 ERROR |
| `warning_level` | 只能取 enum 三个值 | 违反报 ERROR |
| `total_cost_cny` | = total_cost_usd × fx_rate | 偏差 > 1% 报 WARNING |
| `pending_ratio` | [0, 1] | > 0.5 时 Z 分数标注「⚠️ 样本量不足」 |

---

## 五、一致性约束（跨文件）

> validate.py 必须检查以下约束。

| 约束 | 说明 |
|:---|:---|
| **C1 时间基线** | 所有 JSON 的 `_meta.latest_week` 必须一致 |
| **C2 航线集合** | metrics.routes[].code = decisions[].code = history.datasets[].code = {EUR, MED, USWC, USEC, COMPOSITE} |
| **C3 运价锚点** | metrics.current_value = history.datasets[N].data[last] ≠ null |
| **C4 场景锚点** | scenarios.base_freight_usd = metrics 同航线 current_value（USWC/USEC） |
| **C5 预警一致性** | metrics.warning_level 的判定输入应与 decisions 同航线指标一致 |
| **C6 汇率一致性** | 所有 JSON 的 fx_rate 一致 |
