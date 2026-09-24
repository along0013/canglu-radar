# canglu-radar · STATE

> 更新: 2026-09-24

- **阶段**: 可运行 — P0 主链路闭环，CI 绿
- **Git**: github.com/along0013/canglu-radar（main 分支）
- **验证入口**: `python tests/run_smoke_tests.py`（6 组断言，全部通过）
- **CI**: `.github/workflows/smoke.yml`（push / PR 触发）
- **数据快照**: `latest_week = 2026-06-26`，此后未更新
- **关键数字**: `engine/compute.py` 631 行 / `output` 五件套 / Dashboard 六视图
- **阻塞**: 无

## 产出轨迹

| 时间 | 变更 |
|:-----|:-----|
| 2026-05-28 | first commit |
| 2026-06-12 | 用真实数据替换模拟数据（Week2 / Week3 基于上海航交所 06-05、06-12 发布） |
| 2026-08-07 | 首次推送到 GitHub |
| 2026-08-09 | 迁移到标准项目布局，清理比赛遗留目录结构 |
| 2026-09-24 | 补齐依赖声明与 CI 安装步骤，CI 转 `success`；README 重构并补入 Dashboard 截图 |

## 路演材料

路演终版 PPT（`pptxgenjs` 暗色主题，9 页）未随仓库入库；
仓库内保留的是可复现的过程材料，见 `archive/05-presentation/` 与 `archive/08-submission/`。
