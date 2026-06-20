---
生成日期：2026-06-20
版本：正式版
---

# 舱路雷达 | 材料目录

## 提交包结构
舱路雷达/
├── 00-control/              # 控制与QA
│   ├── qa-checklist.md
│   └── batch-map.md
├── 01-raw-data/             # 原始数据（真实+演示补全）
│   ├── freight-index/       # SCFI运价指数
│   ├── exchange-rate/       # 汇率数据
│   ├── carrier-announcements/ # 船公司公告
│   └── surcharge-rules/     # 附加费规则
├── 02-governance/           # 数据治理
│   ├── CR-02A_字段字典.xlsx
│   └── CR-02B_清洗后主数据.xlsx
├── 02-processed-data/       # 处理后数据
│   └── canglu-demo-cost-model-scenario-based.xlsx
├── 03-analysis/             # 指标计算
│   ├── CR-04A_指标计算结果.xlsx
│   └── CR-04C_敏感性分析表.md
├── 04-decision-report/      # 决策建议
│   ├── CR-04B_业务决策建议.md
│   └── CR-05_分析报告.md
├── 05-presentation/         # 展示材料
│   ├── 舱路雷达_参赛展示PPT.pdf
│   └── cr-06-submission-deck.html
├── 06-visual-demo/          # Demo素材
│   ├── CR-07_闭环长图.png
│   └── CR-08_Demo演示脚本.docx
├── 07-validation/           # 量化验证
│   └── CR-09_量化验证表.xlsx
├── 08-submission/           # 提交材料
│   ├── CR-10A_评委阅读指南.md
│   ├── CR-10B_复跑说明.md
│   ├── CR-10C_材料目录.md
│   ├── CR-11_作品说明文档.md
│   └── final-package/
│       └── manifest.csv
└── 09-logs/                 # 复跑记录
├── rerun-records-week2-prime.md
└── rerun-records-week3-prime.md
plain
￼
复制
## 核心文件清单（14个）

| 编号 | 文件 | 用途 | 数据质量 |
|:---|:---|:---|:---|
| 01 | CR-04A_指标计算结果.xlsx | 核心指标源 | A/B/C混合 |
| 02 | CR-04B_业务决策建议.md | 差异化建议 | 基于04A |
| 03 | CR-05_分析报告.md | 分析报告 | 基于04A/04B |
| 04 | CR-09_量化验证表.xlsx | 效率提升证明 | 估算+记录 |
| 05 | 舱路雷达_参赛展示PPT.pdf | 10页参赛展示 | 展示材料 |
| 06 | CR-11_作品说明文档.md | 评审导航 | 说明文档 |
| 07 | CR-10A_评委阅读指南.md | 阅读顺序 | 说明文档 |
| 08 | CR-10B_复跑说明.md | 复跑路径 | 说明文档 |
| 09 | CR-10C_材料目录.md | 文件索引 | 说明文档 |
| 10 | rerun-records-week2-prime.md | 真实复跑记录 | A_official |
| 11 | rerun-records-week3-prime.md | 推算复跑记录 | B_public_excerpt |
| 12 | CR-04C_敏感性分析表.md | what-if分析 | 基于04A |
| 13 | CR-07_闭环长图.png | 一图读懂 | 展示材料 |
| 14 | CR-08_Demo演示脚本.docx | 演示脚本 | 展示材料 |

## 评审建议阅读顺序

1. **3分钟**：打开舱路雷达_参赛展示PPT.pdf，快速理解作品
2. **5分钟**：阅读CR-11_作品说明文档.md，理解评分维度对应关系
3. **10分钟**：打开CR-04A_指标计算结果.xlsx，验证公式和数字
4. **5分钟**：阅读CR-04B_业务决策建议.md，检查差异化建议
5. **5分钟**：阅读rerun-records-week2-prime.md，验证复跑真实性
6. **10分钟**：打开CR-09_量化验证表.xlsx，检查效率提升数据
7. **可选**：打开CR-04C_敏感性分析表.md，查看what-if能力

## 当前状态

所有材料已最终定稿，无占位稿、无待补项、无TODO。
生成日期：2026-06-20。
