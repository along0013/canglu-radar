# CR-10C｜最终版材料目录

本目录基于当前 Git 跟踪文件生成，用于评委快速定位舱路雷达项目材料。草稿、日志、缓存、压缩包和临时抓取页已通过 `.gitignore` 排除，不纳入本目录。

## 1. 总览

- 当前跟踪文件数：190 个
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
| `01-raw-data/collection-reports/current/26-week-placeholder-completeness-summary.csv` | 结构化数据或清单文件。 | B_public_excerpt / C_demo_simulated |
| `01-raw-data/collection-reports/current/26-week-placeholder-file-check.csv` | 结构化数据或清单文件。 | B_public_excerpt / C_demo_simulated |
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
| `01-raw-data/collection-reports/data-source-website-list.csv` | 结构化数据或清单文件。 | B_public_excerpt / C_demo_simulated |
| `01-raw-data/collection-reports/data-source-website-list.md` | Markdown说明、报告或QA材料。 | B_public_excerpt / C_demo_simulated |
| `01-raw-data/collection-reports/document-library-cleanup-recommendations.csv` | 结构化数据或清单文件。 | B_public_excerpt / C_demo_simulated |
| `01-raw-data/collection-reports/document-library-inventory.csv` | 结构化数据或清单文件。 | B_public_excerpt / C_demo_simulated |
| `01-raw-data/collection-reports/document-library-summary.csv` | 结构化数据或清单文件。 | B_public_excerpt / C_demo_simulated |
| `01-raw-data/collection-reports/public-data-write-summary.csv` | 结构化数据或清单文件。 | B_public_excerpt / C_demo_simulated |
| `01-raw-data/data-ingestion-checklist.md` | Markdown说明、报告或QA材料。 | B_public_excerpt / C_demo_simulated |
| `01-raw-data/exchange-rate/usd-cny-screenshot-ocr-daily.csv` | 结构化数据或清单文件。 | B_screenshot_ocr / C_demo_simulated |
| `01-raw-data/exchange-rate/usd-cny-weekly-aligned.csv` | 结构化数据或清单文件。 | B_screenshot_ocr / C_demo_simulated |
| `01-raw-data/exchange-rate/usd-cny-weekly-collection-plan.csv` | 结构化数据或清单文件。 | B_screenshot_ocr / C_demo_simulated |
| `01-raw-data/exchange-rate/usd-cny-weekly-from-screenshot.csv` | 结构化数据或清单文件。 | B_screenshot_ocr / C_demo_simulated |
| `01-raw-data/exchange-rate/week2-input/usd-cny-week2-simulated-input.csv` | 结构化数据或清单文件。 | B_screenshot_ocr / C_demo_simulated |
| `01-raw-data/exchange-rate/week3-input/usd-cny-week3-simulated-input.csv` | 结构化数据或清单文件。 | B_screenshot_ocr / C_demo_simulated |
| `01-raw-data/freight-index/ccfi-weekly-aligned.csv` | 结构化数据或清单文件。 | B_public_excerpt / C_demo_simulated |
| `01-raw-data/freight-index/week2-input/scfi-week2-simulated-input.csv` | 结构化数据或清单文件。 | A_official / B_public_excerpt |
| `01-raw-data/freight-index/week3-input/scfi-week3-simulated-input.csv` | 结构化数据或清单文件。 | A_official / B_public_excerpt |
| `01-raw-data/mvp-raw-files-status.md` | Markdown说明、报告或QA材料。 | B_public_excerpt / C_demo_simulated |
| `01-raw-data/surcharge-rules/README_surcharge_reference_2026_05.md` | Markdown说明、报告或QA材料。 | B_public_excerpt / C_demo_simulated |
| `01-raw-data/surcharge-rules/surcharge-cost-model-reference-input-2026-05.csv` | 结构化数据或清单文件。 | B_public_excerpt / C_demo_simulated |
| `01-raw-data/surcharge-rules/surcharge-market-reference-2026-05.csv` | 结构化数据或清单文件。 | B_public_excerpt / C_demo_simulated |

### 治理层

| 文件路径 | 用途说明 | 数据质量/口径 |
|---|---|---|
| `02-governance/surcharge-scenario-cost-model.md` | Markdown说明、报告或QA材料。 | A/B/C/PENDING 分层治理 |

### 处理层

| 文件路径 | 用途说明 | 数据质量/口径 |
|---|---|---|
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
| `03-analysis/CR-04C_敏感性分析表.md` | 敏感性分析表，展示汇率、附加费和运价上涨的what-if测算能力。 | 基于CR-04A与场景模型公式计算；what-if分析 |
| `03-analysis/rerun-simulations/week2-prime/latest-summary-week2-prime.csv` | 模拟复跑Week2’材料，验证输入变化导致输出变化。 | 由CR-04A数值源计算生成；含A/C/PENDING标注 |
| `03-analysis/rerun-simulations/week3-prime/latest-summary-week3-prime.csv` | 模拟复跑Week3’材料，验证输入变化导致输出变化。 | 由CR-04A数值源计算生成；含A/C/PENDING标注 |

### 展示层

| 文件路径 | 用途说明 | 数据质量/口径 |
|---|---|---|
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

### 提交层

| 文件路径 | 用途说明 | 数据质量/口径 |
|---|---|---|
| `08-submission/CR-10C_材料目录.md` | 最终版材料目录，列出当前仓库跟踪文件。 | 提交/评审导航材料 |
| `08-submission/final-package/manifest.csv` | 提交包清单，列明文件用途和质量口径。 | 提交/评审导航材料 |

### 其他

| 文件路径 | 用途说明 | 数据质量/口径 |
|---|---|---|
| `"01-raw-data/carrier-announcements/\345\216\237\345\247\213_\350\210\271\345\205\254\345\217\270\345\205\254\345\221\212_BAF_ONE.pdf"` | 项目材料。 | N/A |
| `"01-raw-data/carrier-announcements/\345\216\237\345\247\213_\350\210\271\345\205\254\345\217\270\345\205\254\345\221\212_BAF_\350\241\214\344\270\232\350\275\254\350\275\275.txt"` | 项目材料。 | N/A |
| `"01-raw-data/carrier-announcements/\345\216\237\345\247\213_\350\210\271\345\205\254\345\217\270\345\205\254\345\221\212_GRI_\351\251\254\345\243\253\345\237\272.pdf"` | 项目材料。 | N/A |
| `"01-raw-data/carrier-announcements/\345\216\237\345\247\213_\350\210\271\345\205\254\345\217\270\345\205\254\345\221\212_GRI_\351\251\254\345\243\253\345\237\272\345\200\231\351\200\211.txt"` | 项目材料。 | N/A |
| `"01-raw-data/carrier-announcements/\345\216\237\345\247\213_\350\210\271\345\205\254\345\217\270\345\205\254\345\221\212_PSS_\344\270\255\350\277\234.pdf"` | 项目材料。 | N/A |
| `"01-raw-data/carrier-announcements/\345\216\237\345\247\213_\350\210\271\345\205\254\345\217\270\345\205\254\345\221\212_PSS_\351\251\254\345\243\253\345\237\272.txt"` | 项目材料。 | N/A |
| `"01-raw-data/carrier-announcements/\345\216\237\345\247\213_\350\210\271\345\205\254\345\217\270\345\205\254\345\221\212_\345\201\234\350\210\252_MSC.pdf"` | 项目材料。 | N/A |
| `"01-raw-data/carrier-announcements/\345\216\237\345\247\213_\350\210\271\345\205\254\345\217\270\345\205\254\345\221\212_\345\201\234\350\210\252_\347\273\274\345\220\210\350\275\254\350\275\275.txt"` | 项目材料。 | N/A |
| `"01-raw-data/carrier-announcements/\345\216\237\345\247\213_\350\210\271\345\205\254\345\217\270\345\205\254\345\221\212_\347\273\223\346\236\204\345\214\226\346\240\267\346\234\254.csv"` | 项目材料。 | N/A |
| `"01-raw-data/carrier-announcements/\345\216\237\345\247\213_\350\210\271\345\205\254\345\217\270\345\205\254\345\221\212_\350\267\263\346\270\257\346\270\257\345\217\243\346\213\245\345\240\265_MSC\350\275\254\350\275\275.txt"` | 项目材料。 | N/A |
| `"01-raw-data/collection-reports/\345\205\254\345\274\200\346\225\260\346\215\256\350\241\245\351\207\207\347\273\255\346\211\247\350\241\214\346\212\245\345\221\212.md"` | 项目材料。 | N/A |
| `"01-raw-data/collection-reports/current/README_\345\275\223\345\211\215\344\270\273\347\272\277\346\226\207\344\273\266\350\257\264\346\230\216.md"` | 项目材料。 | N/A |
| `"01-raw-data/collection-reports/current/\345\205\254\345\274\200\346\225\260\346\215\256\350\241\245\351\207\207\347\273\255\346\211\247\350\241\214\346\212\245\345\221\212.md"` | 项目材料。 | N/A |
| `"01-raw-data/collection-reports/current/\350\257\212\346\226\255\351\224\231\351\242\230\351\233\206.csv"` | 项目材料。 | N/A |
| `"01-raw-data/collection-reports/current/\350\257\212\346\226\255\351\224\231\351\242\230\351\233\206\344\270\216\345\233\236\345\275\222\346\265\213\350\257\225\346\234\272\345\210\266.md"` | 项目材料。 | N/A |
| `"01-raw-data/collection-reports/current/\350\277\22126\345\221\250\350\210\252\350\277\220\346\214\207\346\225\260\345\275\225\345\205\245\344\270\216\345\215\240\344\275\215\350\257\264\346\230\216.md"` | 项目材料。 | N/A |
| `"01-raw-data/exchange-rate/README_\345\275\223\345\211\215\346\261\207\347\216\207\346\226\207\344\273\266\350\257\264\346\230\216.md"` | 项目材料。 | N/A |
| `"01-raw-data/exchange-rate/\345\216\237\345\247\213_\346\261\207\347\216\207.csv"` | 项目材料。 | N/A |
| `"01-raw-data/exchange-rate/\345\216\237\345\247\213_\346\261\207\347\216\207_\345\205\254\345\274\200\346\240\270\351\252\214\350\241\245\345\205\205.csv"` | 项目材料。 | N/A |
| `"01-raw-data/exchange-rate/\345\216\237\345\247\213_\346\261\207\347\216\207_\345\221\250\345\272\246.csv"` | 项目材料。 | N/A |
| `"01-raw-data/exchange-rate/\345\216\237\345\247\213_\346\261\207\347\216\207_\345\221\250\345\272\246_\346\274\224\347\244\272\350\241\245\345\205\250\347\211\210.csv"` | 项目材料。 | N/A |
| `"01-raw-data/exchange-rate/\345\216\237\345\247\213_\346\261\207\347\216\207_template.csv"` | 项目材料。 | N/A |
| `"01-raw-data/freight-index/\345\216\237\345\247\213_CCFI\350\277\220\344\273\267\346\214\207\346\225\260.csv"` | 项目材料。 | N/A |
| `"01-raw-data/freight-index/\345\216\237\345\247\213_CCFI\350\277\220\344\273\267\346\214\207\346\225\260_\346\274\224\347\244\272\350\241\245\345\205\250\347\211\210.csv"` | 项目材料。 | N/A |
| `"01-raw-data/freight-index/\345\216\237\345\247\213_SCFIS\347\273\223\347\256\227\346\214\207\346\225\260.csv"` | 项目材料。 | N/A |
| `"01-raw-data/freight-index/\345\216\237\345\247\213_SCFIS\347\273\223\347\256\227\346\214\207\346\225\260_\346\274\224\347\244\272\350\241\245\345\205\250\347\211\210.csv"` | 项目材料。 | N/A |
| `"01-raw-data/freight-index/\345\216\237\345\247\213_SCFI\345\215\225\346\234\237\347\273\274\345\220\210\346\214\207\346\225\260.csv"` | 项目材料。 | N/A |
| `"01-raw-data/freight-index/\345\216\237\345\247\213_SCFI\350\277\220\344\273\267\346\214\207\346\225\260.csv"` | 项目材料。 | N/A |
| `"01-raw-data/freight-index/\345\216\237\345\247\213_SCFI\350\277\220\344\273\267\346\214\207\346\225\260_\346\274\224\347\244\272\350\241\245\345\205\250\347\211\210.csv"` | 项目材料。 | N/A |
| `"01-raw-data/freight-index/\345\216\237\345\247\213_\350\210\252\350\277\220\346\214\207\346\225\260_26\345\221\250\345\256\214\346\225\264\345\215\240\344\275\215\351\225\277\350\241\250.csv"` | 项目材料。 | N/A |
| `"01-raw-data/freight-index/\345\216\237\345\247\213_\350\277\220\344\273\267\346\214\207\346\225\260_template.csv"` | 项目材料。 | N/A |
| `"01-raw-data/internal-simulated/\345\216\237\345\247\213_\351\231\204\345\212\240\350\264\271\350\247\204\345\210\231.xlsx"` | 项目材料。 | N/A |
| `"01-raw-data/oil-price/\345\216\237\345\247\213_\345\270\203\344\274\246\347\211\271\345\216\237\346\262\271.csv"` | 项目材料。 | N/A |
| `"01-raw-data/route-dictionary/\345\216\237\345\247\213_\350\210\252\347\272\277\345\255\227\345\205\270.xlsx"` | 项目材料。 | N/A |
| `"01-raw-data/route-dictionary/\345\216\237\345\247\213_\350\210\252\347\272\277\345\255\227\345\205\270_template.csv"` | 项目材料。 | N/A |
| `"01-raw-data/surcharge-rules/\345\216\237\345\247\213_\351\231\204\345\212\240\350\264\271\350\247\204\345\210\231.xlsx"` | 项目材料。 | N/A |
| `"01-raw-data/surcharge-rules/\345\216\237\345\247\213_\351\231\204\345\212\240\350\264\271\350\247\204\345\210\231_template.xlsx"` | 项目材料。 | N/A |
| `"02-governance/CR-02A_\345\255\227\346\256\265\345\255\227\345\205\270.xlsx"` | 项目材料。 | N/A |
| `"02-governance/CR-02A_\345\255\227\346\256\265\345\255\227\345\205\270_template.xlsx"` | 项目材料。 | N/A |
| `"02-governance/CR-02B_\346\270\205\346\264\227\345\220\216\344\270\273\346\225\260\346\215\256.xlsx"` | 项目材料。 | N/A |
| `"02-governance/CR-02B_\346\270\205\346\264\227\345\220\216\344\270\273\346\225\260\346\215\256_template.xlsx"` | 项目材料。 | N/A |
| `"02-governance/CR-02C_\346\225\260\346\215\256\350\204\261\346\225\217\344\270\216\346\235\245\346\272\220\350\257\264\346\230\216.docx"` | 项目材料。 | N/A |
| `"02-processed-data/CR-MVP_\346\225\260\346\215\256\350\264\250\351\207\217\346\243\200\346\237\245.csv"` | 项目材料。 | N/A |
| `"02-processed-data/CR-MVP_\346\270\205\346\264\227\345\220\216\344\270\273\346\225\260\346\215\256.xlsx"` | 项目材料。 | N/A |
| `"03-analysis/CR-04A_\346\214\207\346\240\207\350\256\241\347\256\227\347\273\223\346\236\234.xlsx"` | 指标计算结果，作为项目唯一数值源。 | N/A |
| `"03-analysis/CR-04A_\346\214\207\346\240\207\350\256\241\347\256\227\347\273\223\346\236\234_template.xlsx"` | 指标计算结果，作为项目唯一数值源。 | N/A |
| `"03-analysis/rerun-simulations/week2-prime/CR-04A_\346\214\207\346\240\207\350\256\241\347\256\227\347\273\223\346\236\234_week2-prime.xlsx"` | 指标计算结果，作为项目唯一数值源。 | N/A |
| `"03-analysis/rerun-simulations/week3-prime/CR-04A_\346\214\207\346\240\207\350\256\241\347\256\227\347\273\223\346\236\234_week3-prime.xlsx"` | 指标计算结果，作为项目唯一数值源。 | N/A |
| `"04-decision-report/CR-01_\344\270\232\345\212\241\347\227\233\347\202\271\344\270\216\344\273\267\345\200\274\344\270\273\345\274\240.docx"` | 项目材料。 | N/A |
| `"04-decision-report/CR-01_\344\270\232\345\212\241\347\227\233\347\202\271\344\270\216\344\273\267\345\200\274\344\270\273\345\274\240_outline.md"` | 项目材料。 | N/A |
| `"04-decision-report/CR-03_\345\267\245\344\275\234\346\265\201\350\256\276\350\256\241\350\257\264\346\230\216\344\271\246.docx"` | 项目材料。 | N/A |
| `"04-decision-report/CR-03_\345\267\245\344\275\234\346\265\201\350\256\276\350\256\241\350\257\264\346\230\216\344\271\246_outline.md"` | 项目材料。 | N/A |
| `"04-decision-report/CR-04B_\344\270\232\345\212\241\345\206\263\347\255\226\345\273\272\350\256\256.csv"` | 项目材料。 | N/A |
| `"04-decision-report/CR-04B_\344\270\232\345\212\241\345\206\263\347\255\226\345\273\272\350\256\256.docx"` | 项目材料。 | N/A |
| `"04-decision-report/CR-04B_\344\270\232\345\212\241\345\206\263\347\255\226\345\273\272\350\256\256.md"` | 项目材料。 | N/A |
| `"04-decision-report/CR-04B_\344\270\232\345\212\241\345\206\263\347\255\226\345\273\272\350\256\256_outline.md"` | 项目材料。 | N/A |
| `"04-decision-report/CR-05_\345\210\206\346\236\220\346\212\245\345\221\212.docx"` | 项目材料。 | N/A |
| `"04-decision-report/CR-05_\345\210\206\346\236\220\346\212\245\345\221\212.md"` | 项目材料。 | N/A |
| `"04-decision-report/CR-05_\345\210\206\346\236\220\346\212\245\345\221\212_outline.md"` | 项目材料。 | N/A |
| `"04-decision-report/rerun-simulations/week2-prime/CR-04B_\344\270\232\345\212\241\345\206\263\347\255\226\345\273\272\350\256\256_week2-prime.csv"` | 模拟复跑Week2’材料，验证输入变化导致输出变化。 | N/A |
| `"04-decision-report/rerun-simulations/week2-prime/CR-04B_\344\270\232\345\212\241\345\206\263\347\255\226\345\273\272\350\256\256_week2-prime.docx"` | 模拟复跑Week2’材料，验证输入变化导致输出变化。 | N/A |
| `"04-decision-report/rerun-simulations/week3-prime/CR-04B_\344\270\232\345\212\241\345\206\263\347\255\226\345\273\272\350\256\256_week3-prime.csv"` | 模拟复跑Week3’材料，验证输入变化导致输出变化。 | N/A |
| `"04-decision-report/rerun-simulations/week3-prime/CR-04B_\344\270\232\345\212\241\345\206\263\347\255\226\345\273\272\350\256\256_week3-prime.docx"` | 模拟复跑Week3’材料，验证输入变化导致输出变化。 | N/A |
| `"05-presentation/CR-06_\345\217\202\350\265\233\345\261\225\347\244\272PPT_storyboard.md"` | 项目材料。 | N/A |
| `"05-presentation/CR-06_\345\217\257\346\211\223\345\215\260PPT\347\250\277.md"` | 项目材料。 | N/A |
| `"06-visual-demo/CR-07_\351\227\255\347\216\257\351\225\277\345\233\276.png"` | 项目材料。 | N/A |
| `"06-visual-demo/CR-07_\351\227\255\347\216\257\351\225\277\345\233\276_wireframe.md"` | 项目材料。 | N/A |
| `"06-visual-demo/CR-08_Demo\346\274\224\347\244\272\350\204\232\346\234\254.docx"` | 项目材料。 | N/A |
| `"06-visual-demo/CR-08_Demo\346\274\224\347\244\272\350\204\232\346\234\254_outline.md"` | 项目材料。 | N/A |
| `"07-validation/CR-09_\351\207\217\345\214\226\351\252\214\350\257\201\350\241\250.xlsx"` | 量化验证表，记录效率提升与验证口径。 | N/A |
| `"07-validation/CR-09_\351\207\217\345\214\226\351\252\214\350\257\201\350\241\250_template.xlsx"` | 量化验证表，记录效率提升与验证口径。 | N/A |
| `"08-submission/01_\344\275\234\345\223\201\350\257\264\346\230\216\346\226\207\346\241\243_outline.docx"` | 项目材料。 | N/A |
| `"08-submission/CR-10A_\350\257\204\345\247\224\351\230\205\350\257\273\346\214\207\345\215\227.docx"` | 项目材料。 | N/A |
| `"08-submission/CR-10A_\350\257\204\345\247\224\351\230\205\350\257\273\346\214\207\345\215\227_outline.md"` | 项目材料。 | N/A |
| `"08-submission/CR-10B_\345\244\215\350\267\221\350\257\264\346\230\216.docx"` | 项目材料。 | N/A |
| `"08-submission/CR-10B_\345\244\215\350\267\221\350\257\264\346\230\216_outline.md"` | 项目材料。 | N/A |
| `"08-submission/CR-10C_\346\235\220\346\226\231\347\233\256\345\275\225.docx"` | 项目材料。 | N/A |
| `"08-submission/CR-10C_\346\235\220\346\226\231\347\233\256\345\275\225.md"` | 项目材料。 | N/A |
| `"08-submission/CR-10C_\346\235\220\346\226\231\347\233\256\345\275\225_outline.md"` | 项目材料。 | N/A |
| `"08-submission/CR-11_\344\275\234\345\223\201\350\257\264\346\230\216\346\226\207\346\241\243.md"` | 项目材料。 | N/A |

## 3. 评审建议阅读顺序

| 顺序 | 文件 | 作用 |
|---:|---|---|
| 1 | `08-submission/CR-11_作品说明文档.md` | 评审入口，说明项目闭环、价值、工具整合与限制。 |
| 2 | `03-analysis/CR-04A_指标计算结果.xlsx` | 唯一指标数字源，核对最新周核心数字。 |
| 3 | `04-decision-report/CR-04B_业务决策建议.md` | 查看差异化业务建议、成本场景和公告措辞限制。 |
| 4 | `04-decision-report/CR-05_分析报告.md` | 查看周度分析报告与数据质量限制。 |
| 5 | `03-analysis/CR-04C_敏感性分析表.md` | 查看汇率、附加费和运价上涨敏感性。 |
| 6 | `07-validation/CR-09_量化验证表.xlsx` | 查看效率提升与验证口径。 |
| 7 | `06-visual-demo/demo-screenshots/` | 查看Demo截图素材。 |

## 4. 关键数据质量说明

- `A_official`：官方或结构化可信来源。
- `B_public_excerpt`：公开网页、公告摘录或人工整理公开线索。
- `B_screenshot_ocr`：截图OCR或人工录入复核数据。
- `C_market_reference`：市场参考或场景化附加费输入。
- `C_demo_simulated`：演示补全或模拟复跑数据。
- `PENDING_REVIEW`：待人工复核材料。
