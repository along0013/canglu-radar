# 舱路雷达项目主控执行方案

## 1. 项目定位

项目名称：舱路雷达  
副标题：跨境物流异常预警与发货决策情报台  
目标：面向跨境电商卖家/物流运营岗位，将每周物流情报周报初稿生成从180-240分钟压缩至10-20分钟。

## 2. 已确认调整

1. 批次5《分析报告》输入增加 `CR-02B_清洗后主数据.xlsx`，用于公告事件关联、汇率、附加费和40尺柜成本测算。
2. 批次6《参赛PPT》输入增加 `CR-04B_业务决策建议.docx`，用于PPT第8页发货建议、锁舱建议、报价建议。
3. 批次0数据来源原则上来自公开网站，实际抓取需等待浏览器/网页抓取能力启用后执行。

## 3. 12批次执行地图

| 批次 | 模块 | 执行角色 | 输入 | 输出 | 关键说明 |
|---:|---|---|---|---|---|
| 0 | 样例数据准备 | 主控/数据准备 | 公开网站、模拟规则、航线口径 | 5类原始数据 | 等网页抓取能力启用后执行；模拟数据必须标注 |
| 1 | 业务痛点与价值主张 | 文档顾问 | 业务背景 | `CR-01_业务痛点与价值主张.docx` | 可与批次0并行 |
| 2 | 数据治理 | 数据工程师 | 批次0原始文件 | `CR-02A`、`CR-02B`、`CR-02C` | 数据链路关键底座 |
| 3 | 工作流架构设计 | 企业架构师 | `CR-01`、`CR-02A` | `CR-03_工作流设计说明书.docx` | 描述输入-处理-输出闭环 |
| 4A | 指标计算 | 数据分析师 | `CR-02B` | `CR-04A_指标计算结果.xlsx` | 计算分位、环比、Z分数、连续上涨、预警 |
| 4B | 业务决策映射 | 物流运营顾问 | `CR-04A` | `CR-04B_业务决策建议.docx` | 严格按规则生成建议 |
| 5 | 分析报告 | 情报主编 | `CR-04A`、`CR-04B`、`CR-02B` | `CR-05_分析报告.docx` | 数字必须一致；公告不写因果 |
| 6 | 参赛PPT | PPT设计专家 | `CR-05`、`CR-04A`、`CR-04B` | `CR-06_参赛展示PPT.pptx` | 10页结构，深蓝+橙+白 |
| 7 | 一图读懂长图 | 信息图设计师 | `CR-06`关键页、`CR-05` | `CR-07_闭环长图.png` | 手机端竖版长图 |
| 8 | Demo视频脚本 | Demo导演 | `CR-05`、`CR-06` | `CR-08_Demo演示脚本.docx` | 10分钟时间轴、镜头、旁白、字幕 |
| 9 | 量化验证表 | 数据验证专员 | `CR-04A`、人工基线 | `CR-09_量化验证表.xlsx` | 效率、准确率、商业价值、复跑记录 |
| 10 | 提交材料整理 | 材料整理专家 | 全部前置文件 | `CR-10A/B/C` | 阅读指南、复跑说明、材料目录 |
| 11 | 最终打包检查 | 主控质检 | 全部文件 | ZIP参赛包 | 文件齐全、命名规范、数字一致 |

## 4. 推荐工作区分区

```text
canglu-radar/
├─ 00-control/
│  ├─ project-brief.md
│  ├─ batch-map.md
│  ├─ qa-checklist.md
│  └─ change-log.md
├─ 01-raw-data/
│  ├─ freight-index/
│  ├─ carrier-announcements/
│  ├─ exchange-rate/
│  ├─ surcharge-rules/
│  └─ route-dictionary/
├─ 02-governance/
│  ├─ dictionary/
│  ├─ cleaned-master-data/
│  └─ compliance-notes/
├─ 03-analysis/
│  ├─ metric-calculation/
│  ├─ trend-data/
│  └─ alert-details/
├─ 04-decision-report/
│  ├─ decision-mapping/
│  └─ weekly-report/
├─ 05-presentation/
│  ├─ ppt/
│  └─ export-pdf/
├─ 06-visual-demo/
│  ├─ long-image/
│  ├─ demo-script/
│  └─ video-assets/
├─ 07-validation/
│  ├─ baseline/
│  ├─ quant-verification/
│  └─ rerun-records/
├─ 08-submission/
│  ├─ judge-guide/
│  ├─ rerun-guide/
│  ├─ material-index/
│  └─ final-package/
├─ 09-logs/
│  ├─ web-crawl-log/
│  ├─ data-cleaning-log/
│  ├─ qa-log/
│  └─ issue-log/
└─ 99-archive/
```

## 5. 强制命名与口径

### 文件命名

```text
CR-批次号_模块_描述.扩展名
```

### 核心字段

| 字段 | 含义 |
|---|---|
| `date` | 日期 |
| `route_code` | 航线代码 |
| `route_name` | 航线中文名 |
| `freight_usd` | 运价/费用美元值 |
| `unit` | 单位 |
| `fee_type` | 费用类型 |
| `carrier` | 船公司 |
| `usd_cny_rate` | 汇率 |
| `data_source` | 数据来源 |

### 航线代码

- `CN-USWC`：中国-美西
- `CN-USEC`：中国-美东
- `CN-EUR`：中国-欧洲

## 6. 关键质量控制规则

1. 模拟数据必须标注：本表为基于行业惯例构造的模拟样例数据，仅用于演示工作流能力。
2. 公告关联不判定因果，只使用“高置信关联线索”或“中等关联线索”。
3. `CR-04A`中的分位、环比、Z分数、成本等数字必须与`CR-05`、`CR-06`、`CR-07`保持一致。
4. 数据链路批次2、4A、9必须保持同一字段口径。
5. 每批次结束后都要做文件完整性、命名规范、字段一致性、合规声明检查。

## 7. 推荐执行顺序

```text
批次0 → 批次2 → 批次4A → 批次4B → 批次5 → 批次6 → 批次7/8 → 批次9 → 批次10 → 批次11
```

批次1可与批次0并行；批次3在批次1和批次2A完成后执行。
