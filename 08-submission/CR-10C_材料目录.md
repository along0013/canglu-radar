# CR-10C｜最终版材料目录

本目录基于当前 Git 跟踪文件生成，用于评委快速定位舱路雷达项目材料。草稿、日志、缓存、压缩包和临时抓取页已通过 `.gitignore` 排除，不纳入本目录。

## 1. 总览

- 当前跟踪文件数：189 个
- 核心阅读路径：`CR-11 → CR-04A → CR-04B.md → CR-05.md → CR-04C → CR-09 → CR-10C`
- 数据口径：真实数据、公开线索、演示补全和待复核材料分层标注；含 `C_demo_simulated` 或 `C_market_reference` 的材料仅用于演示和流程验证。

## 2. 分模块材料清单

### 仓库入口

| 文件路径 | 用途说明 | 数据质量/口径 |
|---|---|---|
| `README.md` | 仓库首页与评审阅读导航。 | N/A |

### 仓库配置

| 文件路径 | 用途说明 | 数据质量/口径 |
|---|---|---|
| `.gitignore` | 排除草稿、日志、缓存、压缩包等非评审材料。 | N/A |

### 控制层

| 文件路径 | 用途说明 | 数据质量/口径 |
|---|---|---|
| `00-control/batch-map.md` | Markdown说明、报告或QA材料。 | N/A |
| `00-control/data-dependency-stoplist.md` | Markdown说明、报告或QA材料。 | N/A |
| `00-control/data-governance/README.md` | Markdown说明、报告或QA材料。 | N/A |
| `00-control/data-governance/carrier-announcement-natural-week-rules.txt` | 项目材料。 | N/A |
| `00-control/data-governance/chart-derived-index-c-rules.md` | Markdown说明、报告或QA材料。 | N/A |
| `00-control/data-governance/natural-week-multisource-data-governance.txt` | 项目材料。 | N/A |
| `00-control/data-governance/usd-cny-natural-week-alignment-rules.txt` | 项目材料。 | N/A |
| `00-control/naming-rules.md` | Markdown说明、报告或QA材料。 | N/A |
| `00-control/placeholder-file-index.md` | Markdown说明、报告或QA材料。 | N/A |
| `00-control/qa-checklist.md` | Markdown说明、报告或QA材料。 | N/A |

### 数据层

| 文件路径 | 用途说明 | 数据质量/口径 |
|---|---|---|
| `01-raw-data/carrier-announcements/carrier-announcements-evidence-backlog.csv` | 结构化数据或清单文件。 | B_public_excerpt / PENDING_REVIEW |
| `01-raw-data/carrier-announcements/carrier-announcements-natural-week-events-demo-completed.csv` | 结构化数据或清单文件。 | B_public_excerpt / PENDING_REVIEW |
| `01-raw-data/carrier-announcements/carrier-announcements-natural-week-events.csv` | 结构化数据或清单文件。 | B_public_excerpt / PENDING_REVIEW |
| `01-raw-data/carrier-announcements/week2-input/carrier-announcement-week2-simulated.csv` | 结构化数据或清单文件。 | B_public_excerpt / PENDING_REVIEW |
| `01-raw-data/carrier-announcements/week3-input/carrier-announcement-week3-simulated.csv` | 结构化数据或清单文件。 | B_public_excerpt / PENDING_REVIEW |
| `01-raw-data/carrier-announcements/原始_船公司公告_BAF_ONE.pdf` | 项目材料。 | B_public_excerpt / PENDING_REVIEW |
| `01-raw-data/carrier-announcements/原始_船公司公告_BAF_行业转载.txt` | 项目材料。 | B_public_excerpt / PENDING_REVIEW |
| `01-raw-data/carrier-announcements/原始_船公司公告_GRI_马士基.pdf` | 项目材料。 | B_public_excerpt / PENDING_REVIEW |
| `01-raw-data/carrier-announcements/原始_船公司公告_GRI_马士基候选.txt` | 项目材料。 | B_public_excerpt / PENDING_REVIEW |
| `01-raw-data/carrier-announcements/原始_船公司公告_PSS_中远.pdf` | 项目材料。 | B_public_excerpt / PENDING_REVIEW |
| `01-raw-data/carrier-announcements/原始_船公司公告_PSS_马士基.txt` | 项目材料。 | B_public_excerpt / PENDING_REVIEW |
| `01-raw-data/carrier-announcements/原始_船公司公告_停航_MSC.pdf` | 项目材料。 | B_public_excerpt / PENDING_REVIEW |
| `01-raw-data/carrier-announcements/原始_船公司公告_停航_综合转载.txt` | 项目材料。 | B_public_excerpt / PENDING_REVIEW |
| `01-raw-data/carrier-announcements/原始_船公司公告_结构化样本.csv` | 结构化数据或清单文件。 | B_public_excerpt / PENDING_REVIEW |
| `01-raw-data/carrier-announcements/原始_船公司公告_跳港港口拥堵_MSC转载.txt` | 项目材料。 | B_public_excerpt / PENDING_REVIEW |
| `01-raw-data/collection-reports/current/26-week-placeholder-completeness-summary.csv` | 结构化数据或清单文件。 | B_public_excerpt / C_demo_simulated |
| `01-raw-data/collection-reports/current/26-week-placeholder-file-check.csv` | 结构化数据或清单文件。 | B_public_excerpt / C_demo_simulated |
| `01-raw-data/collection-reports/current/README_当前主线文件说明.md` | Markdown说明、报告或QA材料。 | B_public_excerpt / C_demo_simulated |
| `01-raw-data/collection-reports/current/archive-move-index.csv` | 结构化数据或清单文件。 | B_public_excerpt / C_demo_simulated |
| `01-raw-data/collection-reports/current/coverage-after-chart-10-rounds.csv` | 结构化数据或清单文件。 | B_public_excerpt / C_demo_simulated |
| `01-raw-data/collection-reports/current/coverage-after-chart-10-rounds.md` | Markdown说明、报告或QA材料。 | B_public_excerpt / C_demo_simulated |
| `01-raw-data/collection-reports/current/coverage-difficulties-below-90-after-chart-10-rounds.csv` | 结构化数据或清单文件。 | B_public_excerpt / C_demo_simulated |
| `01-raw-data/collection-reports/current/coverage-report-current.csv` | 结构化数据或清单文件。 | B_public_excerpt / C_demo_simulated |
| `01-raw-data/collection-reports/current/data-source-website-list.csv` | 结构化数据或清单文件。 | B_public_excerpt / C_demo_simulated |
| `01-raw-data/collection-reports/current/data-source-website-list.md` | Markdown说明、报告或QA材料。 | B_public_excerpt / C_demo_simulated |
| `01-raw-data/collection-reports/current/document-library-cleanup-recommendations.csv` | 结构化数据或清单文件。 | B_public_excerpt / C_demo_simulated |
| `01-raw-data/collection-reports/current/document-library-inventory.csv` | 结构化数据或清单文件。 | B_public_excerpt / C_demo_simulated |
| `01-raw-data/collection-reports/current/document-library-summary.csv` | 结构化数据或清单文件。 | B_public_excerpt / C_demo_simulated |
| `01-raw-data/collection-reports/current/final-coverage-after-10-rounds.csv` | 结构化数据或清单文件。 | B_public_excerpt / C_demo_simulated |
| `01-raw-data/collection-reports/current/final-coverage-after-10-rounds.md` | Markdown说明、报告或QA材料。 | B_public_excerpt / C_demo_simulated |
| `01-raw-data/collection-reports/current/post-cleanup-verification.csv` | 结构化数据或清单文件。 | B_public_excerpt / C_demo_simulated |
| `01-raw-data/collection-reports/current/public-data-write-summary.csv` | 结构化数据或清单文件。 | B_public_excerpt / C_demo_simulated |
| `01-raw-data/collection-reports/current/公开数据补采续执行报告.md` | Markdown说明、报告或QA材料。 | B_public_excerpt / C_demo_simulated |
| `01-raw-data/collection-reports/current/诊断错题集.csv` | 结构化数据或清单文件。 | B_public_excerpt / C_demo_simulated |
| `01-raw-data/collection-reports/current/诊断错题集与回归测试机制.md` | Markdown说明、报告或QA材料。 | B_public_excerpt / C_demo_simulated |
| `01-raw-data/collection-reports/current/近26周航运指数录入与占位说明.md` | Markdown说明、报告或QA材料。 | B_public_excerpt / C_demo_simulated |
| `01-raw-data/collection-reports/data-source-website-list.csv` | 结构化数据或清单文件。 | B_public_excerpt / C_demo_simulated |
| `01-raw-data/collection-reports/data-source-website-list.md` | Markdown说明、报告或QA材料。 | B_public_excerpt / C_demo_simulated |
| `01-raw-data/collection-reports/document-library-cleanup-recommendations.csv` | 结构化数据或清单文件。 | B_public_excerpt / C_demo_simulated |
| `01-raw-data/collection-reports/document-library-inventory.csv` | 结构化数据或清单文件。 | B_public_excerpt / C_demo_simulated |
| `01-raw-data/collection-reports/document-library-summary.csv` | 结构化数据或清单文件。 | B_public_excerpt / C_demo_simulated |
| `01-raw-data/collection-reports/public-data-write-summary.csv` | 结构化数据或清单文件。 | B_public_excerpt / C_demo_simulated |
| `01-raw-data/collection-reports/公开数据补采续执行报告.md` | Markdown说明、报告或QA材料。 | B_public_excerpt / C_demo_simulated |
| `01-raw-data/data-ingestion-checklist.md` | Markdown说明、报告或QA材料。 | B_public_excerpt / C_demo_simulated |
| `01-raw-data/exchange-rate/README_当前汇率文件说明.md` | Markdown说明、报告或QA材料。 | B_screenshot_ocr / C_demo_simulated |
| `01-raw-data/exchange-rate/usd-cny-screenshot-ocr-daily.csv` | 结构化数据或清单文件。 | B_screenshot_ocr / C_demo_simulated |
| `01-raw-data/exchange-rate/usd-cny-weekly-aligned.csv` | 结构化数据或清单文件。 | B_screenshot_ocr / C_demo_simulated |
| `01-raw-data/exchange-rate/usd-cny-weekly-collection-plan.csv` | 结构化数据或清单文件。 | B_screenshot_ocr / C_demo_simulated |
| `01-raw-data/exchange-rate/usd-cny-weekly-from-screenshot.csv` | 结构化数据或清单文件。 | B_screenshot_ocr / C_demo_simulated |
| `01-raw-data/exchange-rate/week2-input/usd-cny-week2-simulated-input.csv` | 结构化数据或清单文件。 | B_screenshot_ocr / C_demo_simulated |
| `01-raw-data/exchange-rate/week3-input/usd-cny-week3-simulated-input.csv` | 结构化数据或清单文件。 | B_screenshot_ocr / C_demo_simulated |
| `01-raw-data/exchange-rate/原始_汇率.csv` | 结构化数据或清单文件。 | B_screenshot_ocr / C_demo_simulated |
| `01-raw-data/exchange-rate/原始_汇率_template.csv` | 结构化数据或清单文件。 | B_screenshot_ocr / C_demo_simulated |
| `01-raw-data/exchange-rate/原始_汇率_公开核验补充.csv` | 结构化数据或清单文件。 | B_screenshot_ocr / C_demo_simulated |
| `01-raw-data/exchange-rate/原始_汇率_周度.csv` | 结构化数据或清单文件。 | B_screenshot_ocr / C_demo_simulated |
| `01-raw-data/exchange-rate/原始_汇率_周度_演示补全版.csv` | 结构化数据或清单文件。 | B_screenshot_ocr / C_demo_simulated |
| `01-raw-data/freight-index/ccfi-weekly-aligned.csv` | 结构化数据或清单文件。 | B_public_excerpt / C_demo_simulated |
| `01-raw-data/freight-index/week2-input/scfi-week2-simulated-input.csv` | 结构化数据或清单文件。 | A_official / B_public_excerpt |
| `01-raw-data/freight-index/week3-input/scfi-week3-simulated-input.csv` | 结构化数据或清单文件。 | A_official / B_public_excerpt |
| `01-raw-data/freight-index/原始_CCFI运价指数.csv` | 结构化数据或清单文件。 | B_public_excerpt / C_demo_simulated |
| `01-raw-data/freight-index/原始_CCFI运价指数_演示补全版.csv` | 结构化数据或清单文件。 | B_public_excerpt / C_demo_simulated |
| `01-raw-data/freight-index/原始_SCFIS结算指数.csv` | 结构化数据或清单文件。 | A_official / B_public_excerpt |
| `01-raw-data/freight-index/原始_SCFIS结算指数_演示补全版.csv` | 结构化数据或清单文件。 | A_official / B_public_excerpt |
| `01-raw-data/freight-index/原始_SCFI单期综合指数.csv` | 结构化数据或清单文件。 | A_official / B_public_excerpt |
| `01-raw-data/freight-index/原始_SCFI运价指数.csv` | 结构化数据或清单文件。 | A_official / B_public_excerpt |
| `01-raw-data/freight-index/原始_SCFI运价指数_演示补全版.csv` | 结构化数据或清单文件。 | A_official / B_public_excerpt |
| `01-raw-data/freight-index/原始_航运指数_26周完整占位长表.csv` | 结构化数据或清单文件。 | B_public_excerpt / C_demo_simulated |
| `01-raw-data/freight-index/原始_运价指数_template.csv` | 结构化数据或清单文件。 | B_public_excerpt / C_demo_simulated |
| `01-raw-data/internal-simulated/原始_附加费规则.xlsx` | Excel分析、指标或验证文件。 | B_public_excerpt / C_demo_simulated |
| `01-raw-data/mvp-raw-files-status.md` | Markdown说明、报告或QA材料。 | B_public_excerpt / C_demo_simulated |
| `01-raw-data/oil-price/原始_布伦特原油.csv` | 结构化数据或清单文件。 | B_public_excerpt / C_demo_simulated |
| `01-raw-data/route-dictionary/原始_航线字典.xlsx` | Excel分析、指标或验证文件。 | B_public_excerpt / C_demo_simulated |
| `01-raw-data/route-dictionary/原始_航线字典_template.csv` | 结构化数据或清单文件。 | B_public_excerpt / C_demo_simulated |
| `01-raw-data/surcharge-rules/README_surcharge_reference_2026_05.md` | Markdown说明、报告或QA材料。 | B_public_excerpt / C_demo_simulated |
| `01-raw-data/surcharge-rules/surcharge-cost-model-reference-input-2026-05.csv` | 结构化数据或清单文件。 | B_public_excerpt / C_demo_simulated |
| `01-raw-data/surcharge-rules/surcharge-market-reference-2026-05.csv` | 结构化数据或清单文件。 | B_public_excerpt / C_demo_simulated |
| `01-raw-data/surcharge-rules/原始_附加费规则.xlsx` | Excel分析、指标或验证文件。 | B_public_excerpt / C_demo_simulated |
| `01-raw-data/surcharge-rules/原始_附加费规则_template.xlsx` | Excel分析、指标或验证文件。 | B_public_excerpt / C_demo_simulated |

### 治理层

| 文件路径 | 用途说明 | 数据质量/口径 |
|---|---|---|
| `02-governance/CR-02A_字段字典.xlsx` | Excel分析、指标或验证文件。 | A/B/C/PENDING 分层治理 |
| `02-governance/CR-02A_字段字典_template.xlsx` | Excel分析、指标或验证文件。 | A/B/C/PENDING 分层治理 |
| `02-governance/CR-02B_清洗后主数据.xlsx` | Excel分析、指标或验证文件。 | A/B/C/PENDING 分层治理 |
| `02-governance/CR-02B_清洗后主数据_template.xlsx` | Excel分析、指标或验证文件。 | A/B/C/PENDING 分层治理 |
| `02-governance/CR-02C_数据脱敏与来源说明.docx` | Word文档材料。 | A/B/C/PENDING 分层治理 |
| `02-governance/surcharge-scenario-cost-model.md` | Markdown说明、报告或QA材料。 | A/B/C/PENDING 分层治理 |

### 处理层

| 文件路径 | 用途说明 | 数据质量/口径 |
|---|---|---|
| `02-processed-data/CR-MVP_数据质量检查.csv` | 结构化数据或清单文件。 | A/B/C/PENDING 分层治理 |
| `02-processed-data/CR-MVP_清洗后主数据.xlsx` | Excel分析、指标或验证文件。 | A/B/C/PENDING 分层治理 |
| `02-processed-data/canglu-demo-cost-model-scenario-based.csv` | 结构化数据或清单文件。 | A/B/C/PENDING 分层治理 |
| `02-processed-data/canglu-demo-cost-model-scenario-based.xlsx` | Excel分析、指标或验证文件。 | A/B/C/PENDING 分层治理 |
| `02-processed-data/canglu-radar-scenario-cost-model.xlsx` | Excel分析、指标或验证文件。 | A/B/C/PENDING 分层治理 |
| `02-processed-data/surcharge-scenario-calculation-detail-2026-05.csv` | 结构化数据或清单文件。 | A/B/C/PENDING 分层治理 |
| `02-processed-data/surcharge-scenario-definitions-2026-05.csv` | 结构化数据或清单文件。 | A/B/C/PENDING 分层治理 |
| `02-processed-data/surcharge-scenario-rules-2026-05.csv` | 结构化数据或清单文件。 | A/B/C/PENDING 分层治理 |
| `02-processed-data/surcharge-scenario-summary-2026-05.csv` | 结构化数据或清单文件。 | A/B/C/PENDING 分层治理 |

### 分析层

| 文件路径 | 用途说明 | 数据质量/口径 |
|---|---|---|
| `03-analysis/CR-04A_指标计算结果.xlsx` | 指标计算结果，作为项目唯一数值源。 | 由CR-04A数值源计算生成；含A/C/PENDING标注 |
| `03-analysis/CR-04A_指标计算结果_template.xlsx` | 指标计算结果，作为项目唯一数值源。 | 由CR-04A数值源计算生成；含A/C/PENDING标注 |
| `03-analysis/CR-04C_敏感性分析表.md` | 敏感性分析表，展示汇率、附加费和运价上涨的what-if测算能力。 | 基于CR-04A与场景模型公式计算；what-if分析 |
| `03-analysis/rerun-simulations/week2-prime/CR-04A_指标计算结果_week2-prime.xlsx` | 指标计算结果，作为项目唯一数值源。 | 由CR-04A数值源计算生成；含A/C/PENDING标注 |
| `03-analysis/rerun-simulations/week2-prime/latest-summary-week2-prime.csv` | 模拟复跑Week2’材料，验证输入变化导致输出变化。 | 由CR-04A数值源计算生成；含A/C/PENDING标注 |
| `03-analysis/rerun-simulations/week3-prime/CR-04A_指标计算结果_week3-prime.xlsx` | 指标计算结果，作为项目唯一数值源。 | 由CR-04A数值源计算生成；含A/C/PENDING标注 |
| `03-analysis/rerun-simulations/week3-prime/latest-summary-week3-prime.csv` | 模拟复跑Week3’材料，验证输入变化导致输出变化。 | 由CR-04A数值源计算生成；含A/C/PENDING标注 |

### 决策层

| 文件路径 | 用途说明 | 数据质量/口径 |
|---|---|---|
| `04-decision-report/CR-01_业务痛点与价值主张.docx` | Word文档材料。 | 引用CR-04A与场景模型；含限制说明 |
| `04-decision-report/CR-01_业务痛点与价值主张_outline.md` | Markdown说明、报告或QA材料。 | 引用CR-04A与场景模型；含限制说明 |
| `04-decision-report/CR-03_工作流设计说明书.docx` | Word文档材料。 | 引用CR-04A与场景模型；含限制说明 |
| `04-decision-report/CR-03_工作流设计说明书_outline.md` | Markdown说明、报告或QA材料。 | 引用CR-04A与场景模型；含限制说明 |
| `04-decision-report/CR-04B_业务决策建议.csv` | 结构化数据或清单文件。 | 引用CR-04A与场景模型；含限制说明 |
| `04-decision-report/CR-04B_业务决策建议.docx` | Word版历史交付文件；最终建议以Markdown版为准。 | 引用CR-04A与场景模型；含限制说明 |
| `04-decision-report/CR-04B_业务决策建议.md` | Markdown版业务决策建议，包含差异化建议、成本场景与公告措辞限制。 | 引用CR-04A与场景模型；含限制说明 |
| `04-decision-report/CR-04B_业务决策建议_outline.md` | Markdown说明、报告或QA材料。 | 引用CR-04A与场景模型；含限制说明 |
| `04-decision-report/CR-05_分析报告.docx` | Word版历史交付文件；最终建议以Markdown版为准。 | 引用CR-04A与场景模型；含限制说明 |
| `04-decision-report/CR-05_分析报告.md` | Markdown版分析报告，包含差异化业务建议。 | 引用CR-04A与场景模型；含限制说明 |
| `04-decision-report/CR-05_分析报告_outline.md` | Markdown说明、报告或QA材料。 | 引用CR-04A与场景模型；含限制说明 |
| `04-decision-report/rerun-simulations/week2-prime/CR-04B_业务决策建议_week2-prime.csv` | 模拟复跑Week2’材料，验证输入变化导致输出变化。 | 引用CR-04A与场景模型；含限制说明 |
| `04-decision-report/rerun-simulations/week2-prime/CR-04B_业务决策建议_week2-prime.docx` | 模拟复跑Week2’材料，验证输入变化导致输出变化。 | 引用CR-04A与场景模型；含限制说明 |
| `04-decision-report/rerun-simulations/week3-prime/CR-04B_业务决策建议_week3-prime.csv` | 模拟复跑Week3’材料，验证输入变化导致输出变化。 | 引用CR-04A与场景模型；含限制说明 |
| `04-decision-report/rerun-simulations/week3-prime/CR-04B_业务决策建议_week3-prime.docx` | 模拟复跑Week3’材料，验证输入变化导致输出变化。 | 引用CR-04A与场景模型；含限制说明 |

### 展示层

| 文件路径 | 用途说明 | 数据质量/口径 |
|---|---|---|
| `05-presentation/CR-06_参赛展示PPT_storyboard.md` | Markdown说明、报告或QA材料。 | 展示材料；不新增数据口径 |
| `05-presentation/CR-06_可打印PPT稿.md` | Markdown说明、报告或QA材料。 | 展示材料；不新增数据口径 |
| `05-presentation/PPT_EXPORT_NOTE.md` | Markdown说明、报告或QA材料。 | 展示材料；不新增数据口径 |
| `05-presentation/assets/generated/manifest.json` | 项目材料。 | 展示材料；不新增数据口径 |
| `05-presentation/cr-06-submission-deck.html` | HTML展示或占位材料。 | 展示材料；不新增数据口径 |
| `05-presentation/printable-markdown/README.md` | Markdown说明、报告或QA材料。 | 展示材料；不新增数据口径 |
| `05-presentation/printable-markdown/p1-printable.md` | Markdown说明、报告或QA材料。 | 展示材料；不新增数据口径 |
| `05-presentation/printable-markdown/p2-printable.md` | Markdown说明、报告或QA材料。 | 展示材料；不新增数据口径 |
| `05-presentation/printable-markdown/p3-printable.md` | Markdown说明、报告或QA材料。 | 展示材料；不新增数据口径 |
| `05-presentation/printable-markdown/p4-printable.md` | Markdown说明、报告或QA材料。 | 展示材料；不新增数据口径 |
| `05-presentation/printable-markdown/p5-printable.md` | Markdown说明、报告或QA材料。 | 展示材料；不新增数据口径 |
| `05-presentation/printable-markdown/p6-printable.md` | Markdown说明、报告或QA材料。 | 展示材料；不新增数据口径 |
| `05-presentation/printable-markdown/p7-printable.md` | Markdown说明、报告或QA材料。 | 展示材料；不新增数据口径 |
| `05-presentation/printable-markdown/p8-printable.md` | Markdown说明、报告或QA材料。 | 展示材料；不新增数据口径 |
| `05-presentation/printable-pages/P01.md` | Markdown说明、报告或QA材料。 | 展示材料；不新增数据口径 |
| `05-presentation/printable-pages/P02.md` | Markdown说明、报告或QA材料。 | 展示材料；不新增数据口径 |
| `05-presentation/printable-pages/P03.md` | Markdown说明、报告或QA材料。 | 展示材料；不新增数据口径 |
| `05-presentation/printable-pages/P04.md` | Markdown说明、报告或QA材料。 | 展示材料；不新增数据口径 |
| `05-presentation/printable-pages/P05.md` | Markdown说明、报告或QA材料。 | 展示材料；不新增数据口径 |
| `05-presentation/printable-pages/P06.md` | Markdown说明、报告或QA材料。 | 展示材料；不新增数据口径 |
| `05-presentation/printable-pages/P07.md` | Markdown说明、报告或QA材料。 | 展示材料；不新增数据口径 |
| `05-presentation/printable-pages/P08.md` | Markdown说明、报告或QA材料。 | 展示材料；不新增数据口径 |
| `05-presentation/printable-pages/P09.md` | Markdown说明、报告或QA材料。 | 展示材料；不新增数据口径 |
| `05-presentation/printable-pages/P10.md` | Markdown说明、报告或QA材料。 | 展示材料；不新增数据口径 |
| `05-presentation/screenshots/demo-screenshot-P01.png` | 图片或截图材料。 | 展示材料；不新增数据口径 |
| `05-presentation/screenshots/demo-screenshot-P02.png` | 图片或截图材料。 | 展示材料；不新增数据口径 |
| `05-presentation/screenshots/demo-screenshot-P03.png` | 图片或截图材料。 | 展示材料；不新增数据口径 |
| `05-presentation/screenshots/demo-screenshot-P04.png` | 图片或截图材料。 | 展示材料；不新增数据口径 |
| `05-presentation/screenshots/demo-screenshot-P05.png` | 图片或截图材料。 | 展示材料；不新增数据口径 |
| `05-presentation/screenshots/demo-screenshot-P06.png` | 图片或截图材料。 | 展示材料；不新增数据口径 |
| `05-presentation/screenshots/demo-screenshot-P07.png` | 图片或截图材料。 | 展示材料；不新增数据口径 |
| `05-presentation/screenshots/demo-screenshot-P08.png` | 图片或截图材料。 | 展示材料；不新增数据口径 |
| `05-presentation/screenshots/demo-screenshot-P09.png` | 图片或截图材料。 | 展示材料；不新增数据口径 |
| `05-presentation/screenshots/demo-screenshot-P10.png` | 图片或截图材料。 | 展示材料；不新增数据口径 |
| `06-visual-demo/CR-07_闭环长图.png` | 图片或截图材料。 | 展示材料；不新增数据口径 |
| `06-visual-demo/CR-07_闭环长图_wireframe.md` | Markdown说明、报告或QA材料。 | 展示材料；不新增数据口径 |
| `06-visual-demo/CR-08_Demo演示脚本.docx` | Word文档材料。 | 展示材料；不新增数据口径 |
| `06-visual-demo/CR-08_Demo演示脚本_outline.md` | Markdown说明、报告或QA材料。 | 展示材料；不新增数据口径 |
| `06-visual-demo/demo-assets/demo-narration-subtitles.md` | Markdown说明、报告或QA材料。 | 展示材料；不新增数据口径 |
| `06-visual-demo/demo-screenshots/README.md` | Demo截图素材，用于快速浏览演示流程。 | 展示材料；不新增数据口径 |
| `06-visual-demo/demo-screenshots/demo-screenshot-P01.png` | Demo截图素材，用于快速浏览演示流程。 | 展示材料；不新增数据口径 |
| `06-visual-demo/demo-screenshots/demo-screenshot-P02.png` | Demo截图素材，用于快速浏览演示流程。 | 展示材料；不新增数据口径 |
| `06-visual-demo/demo-screenshots/demo-screenshot-P03.png` | Demo截图素材，用于快速浏览演示流程。 | 展示材料；不新增数据口径 |
| `06-visual-demo/demo-screenshots/demo-screenshot-P04.png` | Demo截图素材，用于快速浏览演示流程。 | 展示材料；不新增数据口径 |
| `06-visual-demo/demo-screenshots/demo-screenshot-P05.png` | Demo截图素材，用于快速浏览演示流程。 | 展示材料；不新增数据口径 |
| `06-visual-demo/demo-screenshots/demo-screenshot-P06.png` | Demo截图素材，用于快速浏览演示流程。 | 展示材料；不新增数据口径 |
| `06-visual-demo/demo-screenshots/demo-screenshot-P07.png` | Demo截图素材，用于快速浏览演示流程。 | 展示材料；不新增数据口径 |
| `06-visual-demo/demo-screenshots/demo-screenshot-P08.png` | Demo截图素材，用于快速浏览演示流程。 | 展示材料；不新增数据口径 |
| `06-visual-demo/demo-screenshots/demo-screenshot-P09.png` | Demo截图素材，用于快速浏览演示流程。 | 展示材料；不新增数据口径 |
| `06-visual-demo/demo-screenshots/demo-screenshot-P10.png` | Demo截图素材，用于快速浏览演示流程。 | 展示材料；不新增数据口径 |

### 验证层

| 文件路径 | 用途说明 | 数据质量/口径 |
|---|---|---|
| `07-validation/CR-09_量化验证表.xlsx` | 量化验证表，新增人工vs自动化对比Sheet，说明时间、错误率、复用性和标准化价值。 | 基于项目实际运行记录和团队经验估算；验证材料 |
| `07-validation/CR-09_量化验证表_template.xlsx` | 量化验证表，新增人工vs自动化对比Sheet，说明时间、错误率、复用性和标准化价值。 | 基于项目实际运行记录和团队经验估算；验证材料 |

### 提交层

| 文件路径 | 用途说明 | 数据质量/口径 |
|---|---|---|
| `08-submission/01_作品说明文档_outline.docx` | Word文档材料。 | 提交/评审导航材料 |
| `08-submission/CR-10A_评委阅读指南.docx` | Word文档材料。 | 提交/评审导航材料 |
| `08-submission/CR-10A_评委阅读指南_outline.md` | Markdown说明、报告或QA材料。 | 提交/评审导航材料 |
| `08-submission/CR-10B_复跑说明.docx` | Word文档材料。 | 提交/评审导航材料 |
| `08-submission/CR-10B_复跑说明_outline.md` | Markdown说明、报告或QA材料。 | 提交/评审导航材料 |
| `08-submission/CR-10C_材料目录.docx` | 最终版材料目录，列出当前仓库跟踪文件。 | 提交/评审导航材料 |
| `08-submission/CR-10C_材料目录.md` | 最终版材料目录，列出当前仓库跟踪文件。 | 提交/评审导航材料 |
| `08-submission/CR-10C_材料目录_outline.md` | 最终版材料目录，列出当前仓库跟踪文件。 | 提交/评审导航材料 |
| `08-submission/CR-11_作品说明文档.md` | 评审入口说明，解释项目闭环、价值、人工vs自动化对比与限制。 | 提交/评审导航材料 |
| `08-submission/final-package/manifest.csv` | 提交包清单，列明文件用途和质量口径。 | 提交/评审导航材料 |

## 3. 评审建议阅读顺序

| 顺序 | 文件 | 作用 |
|---:|---|---|
| 1 | `08-submission/CR-11_作品说明文档.md` | 评审入口，说明项目闭环、价值、工具整合与限制。 |
| 2 | `03-analysis/CR-04A_指标计算结果.xlsx` | 唯一指标数字源，核对最新周核心数字。 |
| 3 | `04-decision-report/CR-04B_业务决策建议.md` | 查看差异化业务建议、成本场景和公告措辞限制。 |
| 4 | `04-decision-report/CR-05_分析报告.md` | 查看周度分析报告与数据质量限制。 |
| 5 | `03-analysis/CR-04C_敏感性分析表.md` | 查看汇率、附加费和运价上涨敏感性。 |
| 6 | `07-validation/CR-09_量化验证表.xlsx` | 查看效率提升、人工vs自动化对比与验证口径。 |
| 7 | `06-visual-demo/demo-screenshots/` | 查看Demo截图素材。 |

## 4. 关键数据质量说明

- `A_official`：官方或结构化可信来源。
- `B_public_excerpt`：公开网页、公告摘录或人工整理公开线索。
- `B_screenshot_ocr`：截图OCR或人工录入复核数据。
- `C_market_reference`：市场参考或场景化附加费输入。
- `C_demo_simulated`：演示补全或模拟复跑数据。
- `PENDING_REVIEW`：待人工复核材料。
