# 舱路雷达｜核心项目骨架文件包

## 说明

本包用于系统性分析“舱路雷达”当前项目骨架，仅整理与项目实际推进直接相关的核心内容：治理规则、项目结构、核心结构化输入、处理后数据、场景化模型、正式/半正式项目文档、当前阶段报告和运行日志。

## 已排除内容

本包有意排除了以下类型文件：

- 截图、图片、OCR切片、证明真实性用的素材；
- 网页探测结果、采集草稿、collection draft 中非结构化证据；
- 临时轮次产物、旧交付压缩包、重复输出包；
- 与当前项目骨架关系较弱的草稿、截图和中间缓存。

## 目录结构

- `00-control/`：项目控制、QA、治理规则；
- `01-raw-data/`：核心结构化输入数据，不含截图证据；
- `02-governance/`：模型治理说明；
- `02-processed-data/`：处理后核心模型和场景化成本结果；
- `05-presentation/`：当前展示材料骨架；
- `09-logs/`：项目运行日志；
- `10-current-output-docs/`：当前更完整的产品方案、工作计划、交接和阶段报告；
- `10-current-output-data/`：当前阶段生成的核心宽表、补全表和质量摘要。

## 文件数量

共纳入核心文件：**30** 个。

## 清单

详见 `manifest.csv`，其中包含原始路径、归类、纳入理由和包内路径。

## 建议阅读顺序

1. `10-current-output-docs/舱路雷达产品方案.txt`
2. `10-current-output-docs/canglu-radar-workplan.md`
3. `00-control/data-governance/README.md`
4. `00-control/data-governance/chart-derived-index-c-rules.md`
5. `02-governance/surcharge-scenario-cost-model.md`
6. `10-current-output-docs/canglu-radar-report.md`
7. `10-current-output-docs/canglu-surcharge-scenario-update.md`
8. `09-logs/run-log.md`
9. 再结合 `02-processed-data/` 与 `10-current-output-data/` 做数据核验。
