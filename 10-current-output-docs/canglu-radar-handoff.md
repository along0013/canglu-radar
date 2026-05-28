# 舱路雷达项目｜当前会话交接说明

> 用途：将本文件交给下一个会话，用于快速恢复项目上下文、识别已完成工作、明确后续继续执行的任务。

---

## 一、项目基本信息

| 项目项 | 内容 |
|---|---|
| 项目名称 | 舱路雷达 |
| 项目定位 | 跨境物流异常预警与发货决策情报台 |
| 核心目标 | 面向跨境电商卖家/物流运营岗位，将每周物流周报初稿生成从180-240分钟压缩至10-20分钟 |
| 当前项目根目录 | `canglu-radar/` |
| 会话历史归档目录 | `canglu-radar-conversations/` |
| 当前状态 | 已完成所有可在无真实公开数据情况下先行完成的骨架类、文档类、说明类、模板类工作；当前停止在“必须等待数据/网络/人工基线输入”的节点 |

---

## 二、用户确认过的关键决策

| 编号 | 决策事项 | 已确认结论 |
|---|---|---|
| D-001 | 项目名称 | 使用“舱路雷达” |
| D-002 | 项目文件夹名称 | 使用英文目录名 `canglu-radar` |
| D-003 | 会话历史目录 | 新增平级目录 `canglu-radar-conversations`，与项目目录互不影响 |
| D-004 | 批次5输入修正 | 批次5《分析报告》输入增加 `CR-02B_清洗后主数据.xlsx`，用于公告事件关联和40尺柜成本测算 |
| D-005 | 批次6输入修正 | 批次6《参赛PPT》输入增加 `CR-04B_业务决策建议.docx`，用于PPT第8页决策建议 |
| D-006 | 数据来源策略 | 批次0数据来源于公开网站，但需要等网页抓取能力/网络连接解决后再执行 |
| D-007 | 模拟数据边界 | 附加费规则表可以模拟构造，但必须标注“基于行业惯例构造的模拟样例数据，仅用于演示工作流能力” |
| D-008 | 会话历史整理 | 当前不急于整理全部会话日志；等项目完成后，用户会统一导出日志，再整理给评委看 |

---

## 三、12批次总体流程

| 批次 | 模块 | 当前状态 | 后续说明 |
|---:|---|---|---|
| 0 | 样例数据准备 | 未正式执行 | 等网络/网页抓取能力开启后，从公开网站抓取运价、公告、汇率等数据 |
| 1 | 业务痛点与价值主张 | 已生成占位正式稿 | 可后续根据用户补充的真实业务细节微调 |
| 2 | 数据治理 | 已生成模板与说明占位稿 | 等批次0数据后生成正式 `CR-02A/B/C` |
| 3 | 工作流架构设计 | 已生成占位正式稿 | 等字段字典和清洗后数据完成后可复核更新 |
| 4A | 指标计算 | 已生成Excel模板 | 等 `CR-02B` 正式数据后计算正式指标 |
| 4B | 业务决策映射 | 已生成占位正式稿 | 等 `CR-04A` 后按规则生成真实建议 |
| 5 | 分析报告 | 已生成占位正式稿 | 等 `CR-04A`、`CR-04B`、`CR-02B` 后更新真实数字和结论 |
| 6 | 参赛PPT | 已生成HTML-first占位骨架和storyboard | 等报告和指标完成后生成正式PPTX |
| 7 | 一图读懂长图 | 已生成HTML占位骨架和wireframe | 等PPT和报告结论确认后生成正式PNG |
| 8 | Demo视频脚本 | 已生成占位正式稿 | 等最终PPT、报告、数据结论后补充具体镜头与数字 |
| 9 | 量化验证表 | 已生成Excel模板 | 等人工基线耗时、人力单价、复核结果后生成正式验证表 |
| 10 | 提交材料整理 | 已生成占位正式稿 | 等全部前置文件完成后补齐页码、文件索引、复验路径 |
| 11 | 最终打包检查 | 未执行 | 等所有文件完成后按 `CR-10C` 目录结构打包 |

---

## 四、当前会话已完成的主要工作

### 1. 完成项目方案理解与拆解

已将用户提供的完整12批次执行方案拆解为：

- 数据准备线；
- 数据治理线；
- 指标计算线；
- 决策建议线；
- 分析报告线；
- PPT/长图/Demo展示线；
- 量化验证线；
- 提交材料整理线；
- 最终打包检查线。

并明确：

- 哪些批次必须串行；
- 哪些批次可以并行；
- 哪些文件是关键输入；
- 哪些环节必须等待真实数据。

---

### 2. 已建立正式项目目录

已创建项目主目录：

```text
canglu-radar/
```

目录结构如下：

```text
canglu-radar/
├─ 00-control/
├─ 01-raw-data/
│  ├─ freight-index/
│  ├─ carrier-announcements/
│  ├─ exchange-rate/
│  ├─ surcharge-rules/
│  └─ route-dictionary/
├─ 02-governance/
├─ 03-analysis/
├─ 04-decision-report/
├─ 05-presentation/
├─ 06-visual-demo/
├─ 07-validation/
├─ 08-submission/
│  └─ final-package/
├─ 09-logs/
└─ 99-archive/
```

---

### 3. 已建立会话历史归档目录

已创建平级目录：

```text
canglu-radar-conversations/
```

目录结构如下：

```text
canglu-radar-conversations/
├─ README.md
├─ 01-full-transcripts/
├─ 02-key-decisions/
│  └─ key-decisions.md
├─ 03-prompts-and-requirements/
├─ 04-reviewer-readable-summary/
│  └─ conversation-summary.md
└─ 99-archive/
```

说明：

- 该目录与正式项目目录平级；
- 只用于保存会话历史、需求变化、关键决策、评委可读摘要；
- 当前暂不整理完整会话，等项目完成后用户会统一导出日志再处理。

---

## 五、已生成的控制类文件

以下文件位于：

```text
canglu-radar/00-control/
```

| 文件 | 状态 | 用途 |
|---|---|---|
| `batch-map.md` | 已完成 | 12批次执行地图 |
| `naming-rules.md` | 已完成 | 文件命名与字段列名规范 |
| `qa-checklist.md` | 已完成 | 数据、合规、交付质量检查清单 |
| `placeholder-file-index.md` | 已完成 | 已生成占位文件索引 |
| `data-dependency-stoplist.md` | 已完成 | 当前停止点与后续数据依赖说明 |

下一个会话恢复项目时，建议首先读取：

```text
canglu-radar/00-control/data-dependency-stoplist.md
canglu-radar/00-control/placeholder-file-index.md
canglu-radar/00-control/batch-map.md
canglu-radar/09-logs/run-log.md
```

---

## 六、已生成的日志类文件

以下文件位于：

```text
canglu-radar/09-logs/
```

| 文件 | 状态 | 用途 |
|---|---|---|
| `run-log.md` | 已完成并已更新 | 记录每批次执行过程和本次骨架工作完成记录 |
| `data-source-log.md` | 已完成模板 | 后续记录公开数据来源、URL、获取日期、数据范围 |
| `issue-log.md` | 已完成模板 | 后续记录问题、异常、处理方式 |

当前 `run-log.md` 已记录：

- 已创建正式项目目录；
- 已创建控制文件、日志模板；
- 已生成原始数据CSV模板、Excel模板、Word占位正式稿、PPT HTML-first骨架、长图HTML骨架；
- 当前停止点为必须等待真实公开数据、人工基线或最终参赛规则。

---

## 七、已生成的原始数据模板

| 文件 | 状态 | 说明 |
|---|---|---|
| `canglu-radar/01-raw-data/freight-index/原始_运价指数_template.csv` | 已完成 | 运价指数CSV模板 |
| `canglu-radar/01-raw-data/exchange-rate/原始_汇率_template.csv` | 已完成 | 汇率CSV模板 |
| `canglu-radar/01-raw-data/route-dictionary/原始_航线字典_template.csv` | 已完成 | 航线字典CSV模板 |
| `canglu-radar/01-raw-data/surcharge-rules/原始_附加费规则_template.xlsx` | 已完成 | 模拟附加费规则Excel模板 |

其中核心字段规范包括：

```text
date
route_code
route_name
freight_usd
unit
fee_type
carrier
usd_cny_rate
data_source
```

航线代码固定为：

```text
CN-USWC：中国-美西
CN-USEC：中国-美东
CN-EUR：中国-欧洲
```

---

## 八、已生成的数据治理与分析模板

| 文件 | 状态 | 说明 |
|---|---|---|
| `canglu-radar/02-governance/CR-02A_字段字典_template.xlsx` | 已完成 | 字段字典Excel模板 |
| `canglu-radar/02-governance/CR-02B_清洗后主数据_template.xlsx` | 已完成 | 清洗后主数据Excel模板，包含运价主表、汇率表、附加费表、公告事件表、航线字典等Sheet |
| `canglu-radar/02-governance/CR-02C_数据脱敏与来源说明.docx` | 已完成占位正式稿 | 说明公开/脱敏/模拟数据边界 |
| `canglu-radar/03-analysis/CR-04A_指标计算结果_template.xlsx` | 已完成 | 指标计算Excel模板，后续填入真实数据后计算分位、环比、Z分数、连续上涨周数和预警标签 |

---

## 九、已生成的决策与报告文档

以下文件位于：

```text
canglu-radar/04-decision-report/
```

| 文件 | 状态 | 说明 |
|---|---|---|
| `CR-01_业务痛点与价值主张.docx` | 已完成占位正式稿 | 当前可读，可后续按真实业务微调 |
| `CR-03_工作流设计说明书.docx` | 已完成占位正式稿 | 已包含输入-处理-输出、五层能力、异常处理等 |
| `CR-04B_业务决策建议.docx` | 已完成占位正式稿 | 等 `CR-04A` 正式指标结果后更新真实建议 |
| `CR-05_分析报告.docx` | 已完成占位正式稿 | 等 `CR-04A`、`CR-04B`、`CR-02B` 后更新真实数字和结论 |

说明：

- 所有需要真实数据的位置均使用 `【待数据填充】` 占位；
- 公告关联部分已明确不能写确定因果，只能写“高置信关联线索”或“中等关联线索”；
- 模拟数据必须声明为演示用途。

---

## 十、已生成的展示类骨架

### 1. PPT相关

| 文件 | 状态 | 说明 |
|---|---|---|
| `canglu-radar/05-presentation/CR-06_参赛展示PPT_storyboard.md` | 已完成 | 10页PPT分镜结构 |
| `canglu-radar/05-presentation/CR-06_参赛展示PPT_placeholder.html` | 已完成 | HTML-first PPT占位源文件 |

注意：

- 当前没有生成正式PPTX；
- 原因是正式PPT需要真实数据、图表和结论；
- 后续应在 `CR-04A`、`CR-04B`、`CR-05` 完成后再生成正式 `CR-06_参赛展示PPT.pptx`。

---

### 2. 长图相关

| 文件 | 状态 | 说明 |
|---|---|---|
| `canglu-radar/06-visual-demo/CR-07_闭环长图_wireframe.md` | 已完成 | 长图内容线框 |
| `canglu-radar/06-visual-demo/CR-07_闭环长图_placeholder.html` | 已完成 | 长图HTML占位骨架 |

后续正式输出应为：

```text
CR-07_闭环长图.png
```

需要等PPT关键页和报告结论确认后生成。

---

### 3. Demo脚本

| 文件 | 状态 | 说明 |
|---|---|---|
| `canglu-radar/06-visual-demo/CR-08_Demo演示脚本.docx` | 已完成占位正式稿 | 已按10分钟时间轴完成结构，后续补真实数字、镜头素材和字幕 |

---

## 十一、已生成的验证与提交材料

| 文件 | 状态 | 说明 |
|---|---|---|
| `canglu-radar/07-validation/CR-09_量化验证表_template.xlsx` | 已完成 | 量化验证Excel模板，等人工基线、人力单价、复核结果后更新 |
| `canglu-radar/08-submission/CR-10A_评委阅读指南.docx` | 已完成占位正式稿 | 等最终文件页码和Sheet位置后补充 |
| `canglu-radar/08-submission/CR-10B_复跑说明.docx` | 已完成占位正式稿 | 等最终执行路径确认后补充 |
| `canglu-radar/08-submission/CR-10C_材料目录.docx` | 已完成占位正式稿 | 等最终文件齐全后更新 |
| `canglu-radar/08-submission/01_作品说明文档_outline.docx` | 已完成占位稿 | 后续可转为正式作品说明文档 |

---

## 十二、当前不能继续推进的事项及原因

| 事项 | 暂停原因 |
|---|---|
| 批次0正式公开数据准备 | 需要网页抓取能力/网络连接解决后，从公开网站抓取数据 |
| 批次2正式数据治理 | 依赖批次0真实原始数据 |
| 批次4A正式指标计算 | 依赖 `CR-02B_清洗后主数据.xlsx` 正式版 |
| 批次4B正式决策建议 | 依赖 `CR-04A_指标计算结果.xlsx` 正式版 |
| 批次5正式分析报告 | 依赖 `CR-04A`、`CR-04B`、`CR-02B` |
| 批次6正式PPT | 依赖报告结论、真实指标、真实决策建议 |
| 批次7正式长图 | 依赖PPT关键页和报告结论 |
| 批次9正式量化验证表 | 依赖人工基线耗时、人力单价、复核结果 |
| 批次10最终提交材料 | 依赖全部前置文件完成 |
| 会话历史整理 | 用户决定项目完成后统一导出日志再整理 |

---

## 十三、下一个会话应优先执行的任务

当用户解决网络/网页抓取问题后，下一个会话应按以下顺序继续：

### 第一步：恢复项目状态

请先读取：

```text
canglu-radar/00-control/data-dependency-stoplist.md
canglu-radar/00-control/placeholder-file-index.md
canglu-radar/00-control/batch-map.md
canglu-radar/09-logs/run-log.md
```

确认：

- 哪些文件已完成；
- 哪些是占位版；
- 哪些必须等待数据；
- 当前是否已有新数据放入 `01-raw-data/`。

---

### 第二步：执行批次0公开数据准备

需要准备或抓取：

```text
原始_运价指数.csv
原始_船公司公告.pdf
原始_汇率.csv
原始_附加费规则.xlsx
原始_航线字典.xlsx
```

注意：

- 运价指数、船公司公告、汇率应尽量来自公开网站；
- 附加费规则可模拟构造，但必须明确标注模拟样例数据；
- 抓取后必须更新 `canglu-radar/09-logs/data-source-log.md`。

---

### 第三步：执行批次2数据治理

输入：

```text
canglu-radar/01-raw-data/ 下的正式原始数据
```

输出正式版：

```text
CR-02A_字段字典.xlsx
CR-02B_清洗后主数据.xlsx
CR-02C_数据脱敏与来源说明.docx
```

要求：

- 日期统一为 `YYYY-MM-DD`；
- 航线统一为 `CN-USWC`、`CN-USEC`、`CN-EUR`；
- 费用统一为 `USD/FEU`；
- 公告PDF抽取为结构化事件表；
- 模拟数据必须声明。

---

### 第四步：执行批次4A指标计算

输入：

```text
CR-02B_清洗后主数据.xlsx
```

输出：

```text
CR-04A_指标计算结果.xlsx
```

计算内容：

- 近26周均值、标准差、最小值、最大值；
- P25、P50、P75、P90、P95、P99；
- 当前分位；
- 周环比；
- Z分数；
- 连续上涨周数；
- 异常预警标签。

---

### 第五步：执行批次4B和批次5

批次4B输入：

```text
CR-04A_指标计算结果.xlsx
```

输出：

```text
CR-04B_业务决策建议.docx
```

批次5输入：

```text
CR-04A_指标计算结果.xlsx
CR-04B_业务决策建议.docx
CR-02B_清洗后主数据.xlsx
```

输出：

```text
CR-05_分析报告.docx
```

注意：

- 所有数字必须与 `CR-04A` 一致；
- 公告关联不能写确定因果；
- 成本测算必须显示公式和汇率取值日期。

---

### 第六步：更新展示材料

输入：

```text
CR-05_分析报告.docx
CR-04A_指标计算结果.xlsx
CR-04B_业务决策建议.docx
```

更新并生成：

```text
CR-06_参赛展示PPT.pptx
CR-07_闭环长图.png
CR-08_Demo演示脚本.docx
```

注意：

- PPT第6-8页必须与 `CR-04A`、`CR-04B`、`CR-05`一致；
- 长图中的数字必须与PPT和报告一致；
- Demo脚本中的字幕和旁白数字不能二次编造。

---

### 第七步：执行批次9、10、11

批次9需要用户提供：

- 人工基线耗时；
- 人力单价；
- 抽样复核结果。

输出：

```text
CR-09_量化验证表.xlsx
```

批次10输出：

```text
CR-10A_评委阅读指南.docx
CR-10B_复跑说明.docx
CR-10C_材料目录.docx
```

批次11：

- 按 `CR-10C` 目录结构整理文件；
- 检查命名、数字一致性、模拟数据声明、公告关联措辞；
- 打包ZIP参赛包。

---

## 十四、必须长期遵守的质量规则

| 规则 | 内容 |
|---|---|
| 字段命名 | 严格使用 `date`、`route_code`、`route_name`、`freight_usd`、`unit`、`fee_type`、`carrier`、`usd_cny_rate`、`data_source` 等规范字段 |
| 航线代码 | 仅使用 `CN-USWC`、`CN-USEC`、`CN-EUR` |
| 单位 | 运价和费用统一为 `USD/FEU` |
| 模拟数据声明 | 附加费规则等模拟数据必须写明“基于行业惯例构造的模拟样例数据，仅用于演示工作流能力” |
| 公告关联措辞 | 只能写“高置信关联线索”或“中等关联线索”，不能写“导致”“因为”等确定因果 |
| 数字一致性 | `CR-04A`中的分位、环比、Z分数、成本等必须与 `CR-05`、`CR-06`、`CR-07`一致 |
| 公式可复核 | `CR-04A`、`CR-09`中的关键指标尽量保留公式，不写死数值 |
| 文件命名 | 遵守 `CR-批次号_模块_描述.扩展名` |
| 日志记录 | 每批次完成后更新 `09-logs/run-log.md` 和必要的数据来源日志 |

---

## 十五、当前会话遗留但暂不处理的事项

以下事项不是遗漏，而是用户明确决定后置：

| 事项 | 当前处理方式 |
|---|---|
| 完整会话日志整理 | 暂不整理，等项目完成后用户统一导出日志再整理 |
| `canglu-radar-conversations/01-full-transcripts/` 完整记录 | 暂空，等日志导出 |
| `canglu-radar-conversations/03-prompts-and-requirements/` 完整Prompt归档 | 暂不处理，等项目完成后统一整理 |
| 评委可读会话证据包 | 后置到项目完成阶段 |

---

## 十六、给下一个会话的建议启动语

用户可以在下一个会话中直接发送：

```text
请先读取 canglu-radar/00-control/data-dependency-stoplist.md、placeholder-file-index.md、batch-map.md 和 09-logs/run-log.md，恢复“舱路雷达”项目状态。
当前网络/网页抓取问题已经解决，请从批次0公开数据准备开始继续执行。
```

如果网络仍未解决，可以发送：

```text
请读取 canglu-radar/00-control/placeholder-file-index.md 和 data-dependency-stoplist.md，检查当前占位文件是否完整，并告诉我还缺哪些非数据类材料。
```

---

## 十七、当前结论

当前会话已完成：

1. 项目方案理解；
2. 12批次任务拆解；
3. 项目目录搭建；
4. 会话归档目录搭建；
5. 控制文件生成；
6. 日志模板生成；
7. 原始数据模板生成；
8. Excel模板生成；
9. Word占位正式稿生成；
10. PPT HTML-first骨架生成；
11. 长图HTML骨架生成；
12. Demo脚本占位稿生成；
13. 提交材料占位稿生成；
14. 数据依赖停止清单生成；
15. 占位文件索引生成；
16. 运行日志更新；
17. 最终检查并停止在必须等待数据的节点。

后续项目可以在公开数据接入后无缝继续。
