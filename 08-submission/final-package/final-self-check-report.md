# 舱路雷达最终收口自检报告

- [x] 3个Word文件是否已替换为正式内容：是
  - 08-submission/CR-10A_评委阅读指南.docx：exists=True，字数=2257，禁用词=无
  - 08-submission/CR-10B_复跑说明.docx：exists=True，字数=2560，禁用词=无
  - 08-submission/CR-10C_材料目录.docx：exists=True，字数=13907，禁用词=无
- [x] manifest与ZIP是否一致：是，差异项数=0，manifest included=193，ZIP文件数=193
- [x] 全局占位词扫描是否通过：是，命中文件数=0
- [x] 复跑说明是否与实际能力对齐：是
- [ ] Git状态是否干净：否。本地 commit 已完成，但 push 因远端凭据过期失败；当前 main ahead origin/main 1 个提交。
- [x] ZIP是否能正常解压：是，testzip=None，空文件数=0

## 关键文件清单
- README.md：存在
- 08-submission/CR-11_作品说明文档.md：存在
- 08-submission/CR-10A_评委阅读指南.docx：存在；Word字数2257；禁用词无
- 08-submission/CR-10B_复跑说明.docx：存在；Word字数2560；禁用词无
- 08-submission/CR-10C_材料目录.docx：存在；Word字数13907；禁用词无
- 03-analysis/CR-04A_指标计算结果.xlsx：存在；sheet=指标结果_数值源,最新周摘要,原始周度宽表,质量等级来源长表,Excel公式审计示例
- 04-decision-report/CR-04B_业务决策建议.md：存在
- 04-decision-report/CR-05_分析报告.md：存在
- 07-validation/CR-09_量化验证表.xlsx：存在；sheet=量化验证表,人工vs自动化对比
- 05-presentation/舱路雷达_参赛展示PPT.pdf：存在

## 阻塞项
- 远端 Git 凭据失效，导致 `git push origin main` 失败。请更新/重新登录 Git 凭据后执行 `git -C "D:/小袁工作/canglu-radar" push origin main`。