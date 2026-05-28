# 舱路雷达｜运行日志

| 批次 | 执行日期 | 输入文件 | 输出文件 | 执行结果 | 备注 |
|---|---|---|---|---|---|
| 0 |  |  |  |  |  |
| 1 |  |  |  |  |  |
| 2 |  |  |  |  |  |
| 3 |  |  |  |  |  |
| 4A |  |  |  |  |  |
| 4B |  |  |  |  |  |
| 5 |  |  |  |  |  |
| 6 |  |  |  |  |  |
| 7 |  |  |  |  |  |
| 8 |  |  |  |  |  |
| 9 |  |  |  |  |  |
| 10 |  |  |  |  |  |
| 11 |  |  |  |  |  |


## 预制作记录

- 已创建正式项目目录、控制文件、日志模板、原始数据CSV模板、文档/PPT/长图/Demo/提交材料占位骨架。真实公开数据抓取后替换占位符。


## 2026-05-28｜骨架类工作完成记录

- 已完成无需真实数据即可先行制作的控制文件、日志文件、CSV模板、Excel模板、Word占位正式稿、PPT HTML-first骨架、长图HTML骨架、提交材料占位稿。
- 当前停止点：后续所有实质更新均依赖公开网站数据抓取、人工基线耗时或最终参赛提交规则。
- 数据接入后可从 `00-control/data-dependency-stoplist.md` 所列顺序无缝启动。

## 2026-05-28｜状态恢复记录

- 已读取交接文件 `output/canglu-radar-handoff.md` 与 `00-control/` 下控制文件，确认项目采用“12批次执行地图 + 数据依赖停止清单 + 命名规范 + QA清单”推进。
- 当前项目状态：骨架类产物已完成；`01-raw-data/` 仅发现模板型原始数据，`02-processed-data/` 尚未创建；实质数据治理、指标计算、报告定稿均依赖公开数据接入。
- 当前继续执行策略：不使用模板数据冒充真实结果；下一步应先接入或抓取运价指数、船司公告、汇率与航线字典等公开数据，再从批次0/2启动治理。

## 2026-05-28｜MVP原始文件采集与最小治理记录

- 已按“先跑通工作流MVP”原则落地7个原始输入文件：SCFI运价指数、USD/CNY汇率、4份船司公告PDF、附加费规则表。
- 已生成最小治理产物：`02-processed-data/CR-MVP_清洗后主数据.xlsx`、`02-processed-data/CR-MVP_数据质量检查.csv`、`02-governance/CR-02A_字段字典.xlsx`、`02-governance/CR-02B_清洗后主数据.xlsx`。
- 数据质量说明：SCFI含5个公开转载可核验周度点，其余周显式标记待补；汇率和附加费规则为MVP模拟/占位数据；部分船司公告为公开网页快照或fallback快照，后续需替换为目标船司官方PDF/网页打印件。
- 执行结论：MVP数据链路已可跑通，但正式分析结论仍需替换真实数据后再生成。

## 2026-05-28｜完整数据采集清单执行记录

- 已按用户提供的完整采集清单逐项执行并生成报告：`01-raw-data/collection-reports/完整数据采集执行报告.md` 与 `.csv`。
- 已确认上海航运交易所 SCFI/CCFI/SCFIS 多期接口 `/index/mutipleIndex` 可定位，但当前无登录态返回“对不起你没有登陆”，未能合规批量取得官方历史数据。
- 已尝试 Yahoo、FRED、Stooq、东方财富等汇率/油价备用行情源；当前网络/接口限制导致 USD/CNY 官方中间价与布伦特周度数据未成功真实落地。
- 已保存若干船司公告候选/转载文本，其中 Maersk PSS 为官方网页文本；停航、跳港、BAF等仍需后续用网桥获取目标船司官方网页/PDF。
- 已完成 Tier 3 模拟附加费规则表和航线字典，均按要求标注或说明模拟/自行整理属性。
- 下一步建议：优先用网桥携带浏览器登录态访问上海航交所多期查询和中国货币网中间价页面，替换当前缺失/模拟数据。


## 2026-05-28 公开数据补采续执行

- 执行原则：优先公开、无需注册、不付费；不将模拟数据伪装为真实数据。
- 已更新：SCFI近期公开转引记录、SCFIS 4期公开轨迹值、SAFE USD/CNY单日官方记录、Brent公开快讯价点、船司公告结构化样本。
- 生成报告：`01-raw-data/collection-reports/公开数据补采续执行报告.md`。
- 当前阻塞：SCFI/CCFI/SCFIS完整历史批量数据仍受上海航运交易所多期查询登录/授权限制；USD/CNY和Brent完整26周序列仍需人工导出或替代源。
- 后续建议：走“单期逐周采集 + 二手公开转引补缺 + 质量等级标注”的路线。


## 2026-05-28 单期逐周采集准确性控制

- 用户确认：网页正文可截图/保存为图片，不强求PDF；继续单期逐周下载，注意数据录入准确度。
- 已建立26周逐周采集台账：`01-raw-data/collection-drafts/manual-weekly/weekly-single-query-plan.csv`。
- 已保存官方单期页探测结果，但发现历史日期提交无法可靠回显目标日期，且SCFI分航线值多为空；为避免错录，不作为批量历史录入依据。
- 已保存新浪财经/维运网周报正文证据：`01-raw-data/collection-drafts/manual-weekly/sina-2026-05-26-scfi.txt`。
- 已生成高置信草稿：`01-raw-data/collection-drafts/manual-weekly/verified-weekly-index-records.csv`，完成2026-05-22 SCFI综合、欧洲、地中海、美西、美东五项值。
- 2026-05-15和2026-05-08虽有公开数值线索，但本轮未保存到可复核网页正文，暂标记为二次核验待办，未纳入高置信草稿。


## 2026-05-28 文档库非删除式整理与诊断错题集

- 已执行非删除式整理：旧报告、诊断文件、探测HTML/CSV移动到 `01-raw-data/collection-reports/archive/`，未删除文件。
- 已建立当前主线目录：`01-raw-data/collection-reports/current/`。
- 已生成当前主线说明：`01-raw-data/collection-reports/current/README_当前主线文件说明.md`。
- 已生成归档移动索引：`01-raw-data/collection-reports/current/archive-move-index.csv`。
- 已生成诊断错题集：`01-raw-data/collection-reports/current/诊断错题集.csv`。
- 已生成错题集机制说明：`01-raw-data/collection-reports/current/诊断错题集与回归测试机制.md`。
- 后续原则：错题测试只在空闲时优化路径，不阻塞主线；若问题解决，必须回填 resolved_method 和 status。


## 2026-05-28 近26周航运指数占位录入

- 已按用户要求继续录入近26周数据；未搜到或证据不足的周次统一保留占位符。
- 更新文件：
  - `01-raw-data/freight-index/原始_SCFI运价指数.csv`
  - `01-raw-data/freight-index/原始_CCFI运价指数.csv`
  - `01-raw-data/freight-index/原始_SCFIS结算指数.csv`
  - `01-raw-data/freight-index/原始_航运指数_26周完整占位长表.csv`
  - `01-raw-data/collection-reports/current/26-week-placeholder-completeness-summary.csv`
  - `01-raw-data/collection-reports/current/近26周航运指数录入与占位说明.md`
- 当前覆盖情况：SCFI 26行中7行有值、19行占位；CCFI 26行中2行有值、24行占位；SCFIS 30行中4行有值、26行占位。
- 占位行统一标记：`record_status=placeholder_pending`，`data_quality_level=PENDING`，不得作为真实数据参与正式分析。

## 2026-05-28｜新会话接续：SCFI 2026-05-15/2026-05-08 证据复核

- 已按交接表读取主线说明、占位规则、26周采集台账、SCFI主表、统一长表和诊断错题集，未重复执行文件整理。
- 搜索接口本轮连续返回 MCP 执行失败，未将其视为“无数据”结论；改为检索项目本地归档证据。
- 2026-05-15：在 `01-raw-data/collection-reports/archive/old-reports/sse_single_scfi_2026-05-15_table_0.csv` 中确认官方单期表记录：SCFI综合指数上期 2026-05-15 = 2140.66；但分航线值为空。
- 2026-05-08：本地未找到可复核网页正文、截图或官方页面证据；现有数值仍按 PENDING/二次核验处理。
- 已同步保守更新：`原始_SCFI运价指数.csv`、`原始_航运指数_26周完整占位长表.csv`、`weekly-single-query-plan.csv`。本轮未新增高置信分航线记录，未把搜索摘要或未核验数值升级为真实证据。

## 2026-05-28｜规则口径更新：自然周级多源分层治理

- 用户指出此前整理方法过于单一和严苛，已上传新的总办法与两个细则。
- 已将三份规则从 `output/` 非删除式复制到 `00-control/data-governance/`，作为后续补采入口：
  - `natural-week-multisource-data-governance.txt`
  - `carrier-announcement-natural-week-rules.txt`
  - `usd-cny-natural-week-alignment-rules.txt`
  - `README.md`
- 后续执行口径调整为：以自然周为统一颗粒度，多源互补，字段分层采集；只要 P0 字段可确定即可保留记录，缺失字段标记 NA，不再因局部字段缺失整行搁置。
- 真实主表与演示补全表分开：A/B级进入真实主表，C级/插值仅进入演示补全版并明确标注。
- 船公司公告按发布日期归入自然周，生效日期另列；汇率按自然周最后一个交易日代表值对齐。

## 2026-05-28｜双方向同步补充：指数线索层、汇率周对齐、船司公告自然周事件表

- 按用户要求开始双方向同步补充：方向一为航运指数自然周线索治理，方向二为汇率周对齐与船司公告自然周事件治理。
- 方向一：新增/更新 `01-raw-data/collection-drafts/manual-weekly/scfi-weekly-clues.csv`，将 2026-05-08、2026-05-01、2026-04-24 的 SCFI 已有数值作为线索层集中管理；未找到可复核正文/截图前仍为 PENDING，不升级真实主表质量。同步更新 `weekly-single-query-plan.csv` 的 scfi_status 和 notes。
- 方向二-汇率：新增/更新 `01-raw-data/exchange-rate/usd-cny-weekly-aligned.csv`。2026-05-18 至 2026-05-24 自然周使用已核验 SAFE 记录 USD/CNY=6.8373；2026-05-11、2026-05-04 两个自然周保留 PENDING。
- 方向二-船司公告：新增/更新 `01-raw-data/carrier-announcements/carrier-announcements-natural-week-events.csv`。因现有样本缺少公告发布日期，暂按 effective_date 归入生效自然周，并保留缺失原因，待后续补公告发布日期后可重算公告自然周。
- 本轮遵循自然周多源分层治理新口径：能确定字段先入库，缺失字段标注原因；A/B 与 PENDING/C 不混用。

## 2026-05-28｜继续采集补全：指数公开摘录入库、汇率周度表、公告证据待补清单

- 联网搜索工具本轮仍连续返回 MCP tool execution failed，因此未把搜索失败视为无数据；转为使用项目内 batch-01 已保存公开摘录草稿和现有结构化样本。
- 指数方向：按新自然周多源分层治理口径，将 batch-01 中 2026-04-17、2026-04-24、2026-05-01、2026-05-08 的 SCFI 明确数值补入 `原始_SCFI运价指数.csv` 和 `原始_航运指数_26周完整占位长表.csv`，质量标记为 `B_pending_original_text`；2026-05-15 保持综合指数官方A、分航线公开摘录待原文复核。
- 指数线索层：同步更新 `collection-drafts/manual-weekly/scfi-weekly-clues.csv` 和 `weekly-single-query-plan.csv`，用于后续补原文/截图。
- 汇率方向：新增/更新 `exchange-rate/原始_汇率_周度.csv`，按细则形成周度主表。目前 2026-W21 使用 SAFE 已核验值 6.8373，2026-W19/W20 保持 PENDING。
- 船司公告方向：新增 `carrier-announcements/carrier-announcements-evidence-backlog.csv`，列出公告发布日期、原文URL/正文待补项，便于后续按公告自然周重算。
- 本轮未使用模拟值、未插值，未将待原文复核数据标为官方A。

## 2026-05-28｜扩大搜索面补充：本地全项目检索、公告日期回填、CCFI周表与汇率26周计划

- 按用户要求继续扩大搜索面。联网搜索仍不可用，因此执行项目内全量本地检索，覆盖 csv/txt/md/html/json，检索结果清单已保存至 `01-raw-data/collection-drafts/manual-weekly/expanded-local-search-inventory.csv`。
- SCFI：对旧有数值记录 2026-03-13、2026-03-20、2026-04-10 补充质量等级与状态，标记为 `B_pending_source_recheck`，避免旧值无等级混入分析。当前 SCFI 非空/非PENDING质量记录约 9 行。
- CCFI：新增/更新 `01-raw-data/freight-index/ccfi-weekly-aligned.csv`，将 26 周 CCFI 按自然周统一对齐，并将已有值同步到统一长表；缺失周保持 PENDING。
- 船司公告：从 Maersk 官方 URL 路径解析并回填 3 条公告发布日期，计算公告自然周；公告证据待补清单从 4 条降至 1 条，仍待补 MSC 公告日期/原文证据。
- 汇率：新增/更新 `01-raw-data/exchange-rate/usd-cny-weekly-collection-plan.csv`，形成 26 周 USD/CNY 采集计划；已核验周 1 条，其余保持 PENDING。
- 本轮未使用模拟值、未插值，所有扩展补充均保留来源层级和待核验说明。

## 2026-05-28｜10轮搜索与覆盖率收口

- 已按用户要求执行最多10轮搜索/录入。真实/公开覆盖率未超过95%；含演示补全层覆盖率达到95%以上。
- 最终覆盖率报告：`01-raw-data/collection-reports/current/final-coverage-after-10-rounds.md` 与 `.csv`。
- 所有 C_demo 数据均单独保存在演示补全版文件，不覆盖真实主表。

## 图表反推数据治理与示例入表
- 将用户提供的上海航运交易所指数图表示例纳入 C 级参考数据治理。
- 新增规则：`canglu-radar/00-control/data-governance/chart-derived-index-c-rules.md`。
- 新增/更新记录表：`canglu-radar/01-raw-data/collection-drafts/chart-evidence/chart-derived-index-records.csv`。
- 已录入 C 级图表参考记录：CCFI 2026-05-22 综合指数 1317.36；SCFIS 2026-05-25 欧洲航线 1863.74；SCFIS 2026-05-25 美西航线 1960.27。
- 这些记录均标记为 `C_chart_reference`，只进入图表参考层，不覆盖 A/B 真实主表。
- 外部搜索接口本轮仍失败，后续可通过浏览器复现上海航运交易所图表页面或继续上传截图扩展该层数据。

## 继续10轮：图表参考法扩展补全
- 按用户要求继续执行10轮搜索/探测/录入，标准与前轮一致：超过95%提前停，否则10轮后输出覆盖率和困难点。
- 外部web_search仍失败，但通过直接解析上海航运交易所页面发现 `indexImg` 图表接口。
- 批量生成并保存CCFI、SCFIS欧洲、SCFIS美西图表PNG证据；tooltip读数按 `C_chart_reference` 合并入图表参考层。
- 未将C级图表值覆盖A/B真实主表；汇率未新增未核验值。
- 覆盖率报告已输出至 `canglu-radar/01-raw-data/collection-reports/current/coverage-after-chart-10-rounds.md`。

## 停止外部搜索后的汇率截图录入与航运图表策略调整
- 按用户指令停止外部搜索。
- 航运指数后续缺口统一接受图表估算/tooltip读取作为 `C_chart_reference`，不再强求 CCFI/SCFIS A/B 层补采。
- 识别用户上传长图 `output/半年汇率表.png`，表头为中国外汇交易中心历史参考汇率，字段包含多时点参考汇率。
- 已从切片OCR中提取日频记录 89 条，并按自然周最后可见交易日生成周度代表值 19 条。
- 已更新 `canglu-radar/01-raw-data/exchange-rate/原始_汇率_周度.csv` 与 `usd-cny-weekly-collection-plan.csv`。
- 汇率记录质量标记为 `B_screenshot_ocr_official_page` 或 `B_screenshot_ocr_header_inferred`，建议人工抽样复核。


## 附加费参考行情接入（用户提供 2026年5月底行情）
- 已读取 `output/附加费明细.txt`，将其作为 2026年5月底海运附加费参考行情接入。
- 结构化输出：
  - `canglu-radar/01-raw-data/surcharge-rules/surcharge-market-reference-2026-05.csv`
  - `canglu-radar/01-raw-data/surcharge-rules/surcharge-cost-model-reference-input-2026-05.csv`
- 已在 `原始_附加费规则.xlsx` 中新增/替换 `2026_market_reference` 工作表，保留原模拟样例工作表。
- 数据质量：统一标记为 `C_market_reference`；来源为用户提供市场参考文本，未附官方船司报价单/合同/网页证据，因此不进入 A/B 真实费率层。
- 使用规则：可进入演示成本测算、敏感性分析和参数占位；正式测算前需由用户补充合同价、船司官网公告、报价单或业务系统导出的脱敏费率表。

## 附加费场景化模型修正

| 批次 | 执行日期 | 输入文件 | 输出文件 | 执行结果 | 备注 |
|---|---|---|---|---|---|
| surcharge-scenario-2026-05 | 2026-05-28 | `01-raw-data/surcharge-rules/surcharge-cost-model-reference-input-2026-05.csv`; `output/canglu-freight-indicators-wide.csv`; `output/canglu-fx-weekly-demo-aligned.csv` | `02-processed-data/surcharge-scenario-rules-2026-05.csv`; `02-processed-data/surcharge-scenario-summary-2026-05.csv`; `02-processed-data/canglu-demo-cost-model-scenario-based.csv`; `02-governance/surcharge-scenario-cost-model.md` | 完成 | 将旧版附加费简单求和修正为场景化规则模型。基础场景836.50 USD/FEU；压力场景2,111.50 USD/FEU；美东巴拿马压力场景2,386.50 USD/FEU。来源仍为C_market_reference，仅用于演示测算。 |

