# 舱路雷达｜当前主线文件说明

本次已执行“非删除式整理”：旧报告、诊断文件、探测HTML/CSV被移动到 `collection-reports/archive/` 下；正式原始数据、关键证据、逐周采集台账仍保留在原业务目录。

## 当前最应该看的文件

### 1. 逐周采集主线

- `01-raw-data/collection-drafts/manual-weekly/weekly-single-query-plan.csv`  
  最近26周逐周采集台账。

- `01-raw-data/collection-drafts/manual-weekly/verified-weekly-index-records.csv`  
  已核验、可追溯的周度高置信草稿数据。

- `01-raw-data/collection-drafts/manual-weekly/single-week-collection-progress.md`  
  当前逐周采集阶段说明。

### 2. 当前报告与清单

- `01-raw-data/collection-reports/current/公开数据补采续执行报告.md`
- `01-raw-data/collection-reports/current/data-source-website-list.md`
- `01-raw-data/collection-reports/current/document-library-cleanup-recommendations.csv`
- `01-raw-data/collection-reports/current/archive-move-index.csv`

### 3. 正式/半正式原始数据

- `01-raw-data/freight-index/原始_SCFI运价指数.csv`
- `01-raw-data/freight-index/原始_CCFI运价指数.csv`
- `01-raw-data/freight-index/原始_SCFIS结算指数.csv`
- `01-raw-data/exchange-rate/原始_汇率.csv`
- `01-raw-data/oil-price/原始_布伦特原油.csv`
- `01-raw-data/carrier-announcements/原始_船公司公告_结构化样本.csv`

## 归档区说明

- `01-raw-data/collection-reports/archive/diagnostics/`：接口测试、网页探测、失败诊断等文件。
- `01-raw-data/collection-reports/archive/old-reports/`：旧阶段报告。
- `01-raw-data/collection-reports/archive/old-inventories/`：旧清单/状态摘要。
- `01-raw-data/collection-reports/archive/draft-probes/`：早期探测HTML、搜索缓存、结构分析草稿。

## 原则

- 不删除文件，只归档移动。
- 新采集数据必须有证据正文、截图或网页缓存。
- 诊断失败不直接丢弃，沉淀到“错题集”，后续空闲时回归测试。
