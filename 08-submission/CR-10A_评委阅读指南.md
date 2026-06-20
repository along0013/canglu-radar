# CR-10A 评委阅读指南

## 一、阅读目标
本指南用于帮助评审在较短时间内把握“舱路雷达”的项目价值、材料结构与核验路径。建议先看结论与核心文件，再按材料目录深入核验数据、指标和业务建议。

## 7. 评审速读结论

1. **场景真实**：围绕跨境物流运营每周实际要做的运价查询、成本测算和发货建议展开。
2. **链路闭环**：从原始数据、清洗治理、指标计算到建议、报告、展示和复跑说明均有文件支撑。
3. **数字一致**：核心数字统一来自 `03-analysis/CR-04A_指标计算结果.xlsx`。
4. **建议已差异化**：`CR-04B_业务决策建议.md` 和 `CR-05_分析报告.md` 已按欧洲、地中海、美西、美东、SCFI 生成不同建议。
5. **限制透明**：所有演示补全、模拟复跑、公告关联和附加费参考口径均保留质量标记和使用边界。

### 6.1 核心文件索引

| 文件 | 路径 | 一句话说明 |
|---|---|---|
| 指标计算结果 | `03-analysis/CR-04A_指标计算结果.xlsx` | 所有核心数字的唯一来源。 |
| Markdown 业务建议 | `04-decision-report/CR-04B_业务决策建议.md` | 最新周预警、差异化建议、成本场景和公告措辞限制。 |
| Markdown 分析报告 | `04-decision-report/CR-05_分析报告.md` | 周度分析报告，包含差异化业务建议。 |
| 复跑 Week2' | `03-analysis/rerun-simulations/week2-prime/CR-04A_指标计算结果_week2-prime.xlsx` | 第二次输入替换后的指标输出。 |
| 复跑 Week3' | `03-analysis/rerun-simulations/week3-prime/CR-04A_指标计算结果_week3-prime.xlsx` | 第三次输入替换后的指标输出。 |
| 量化验证表 | `07-validation/CR-09_量化验证表.xlsx` | 效率、质量和复用性验证框架。 |
| PPT storyboard | `05-presentation/CR-06_参赛展示PPT_storyboard.md` | 展示页结构与讲述逻辑。 |
| HTML 展示页 | `05-presentation/cr-06-submission-deck.html` | 浏览器可查看的展示材料。 |
| 闭环长图 | `06-visual-demo/CR-07_闭环长图.png` | 展示从数据到建议的闭环链路。 |
| Demo 脚本 | `06-visual-demo/CR-08_Demo演示脚本.docx` | 演示旁白和流程。 |
| 评委阅读指南 | `08-submission/CR-10A_评委阅读指南.docx` | 评委快速阅读顺序。 |
| 复跑说明 | `08-submission/CR-10B_复跑说明.docx` | 说明如何复跑和比对结果。 |
| 材料目录 | `08-submission/CR-10C_材料目录.docx`、`08-submission/CR-10C_材料目录_outline.md` | 提交材料索引。 |
| 提交包清单 | `08-submission/final-package/manifest.csv` | final-package 中的材料清单。 |

## 二、建议阅读顺序
1. 阅读 `08-submission/CR-11_作品说明文档.md`，了解项目定位、业务场景、数据质量分层和闭环链路。
2. 打开 `03-analysis/CR-04A_指标计算结果.xlsx`，核对关键指标、周度变化与分析结论来源。
3. 阅读 `04-decision-report/CR-04B_业务决策建议.md`，查看业务建议如何引用指标结果。
4. 阅读 `04-decision-report/CR-05_分析报告.md`，理解分析过程、风险判断和适用边界。
5. 打开 `07-validation/CR-09_量化验证表.xlsx`，核验效率、价值和材料完整性验证口径。
6. 最后阅读 `08-submission/CR-10C_材料目录.md`，按目录追溯全部交付材料。

## 三、评审关注点
- 数据真实性：区分官方公开、公开摘录、市场参考和演示数据，避免混用。
- 指标闭环：从原始数据到计算结果、业务建议和展示材料应保持一致。
- 商业价值：关注人工流程替代、响应速度提升和管理层决策支持能力。
- 可复核性：当前项目支持离线材料级复核，所有核心文件均随提交包提供。

## 四、关键文件入口
- `README.md`：项目首页与阅读顺序。
- `08-submission/CR-11_作品说明文档.md`：作品主说明。
- `03-analysis/CR-04A_指标计算结果.xlsx`：指标计算结果。
- `04-decision-report/CR-04B_业务决策建议.md`：业务决策建议。
- `04-decision-report/CR-05_分析报告.md`：分析报告。
- `05-presentation/舱路雷达_参赛展示PPT.pdf`：10页展示材料。
- `07-validation/CR-09_量化验证表.xlsx`：验证表。
- `08-submission/CR-10B_复跑说明.docx`：材料级复核说明。
- `08-submission/CR-10C_材料目录.docx`：材料目录。
