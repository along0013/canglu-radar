# 舱路雷达 canglu-radar

舱路雷达是一个面向跨境物流与供应链决策的异常预警系统。它把运价指数、汇率、油价、事件与附加费场景等数据统一计算成可交付的 `output` 五件套，并提供 Dashboard 展示、数据校验、复算验证和 CI smoke tests。

项目最早用于 OPC 路演场景；比赛已经结束，当前 README 以项目现有功能和工程化验证能力为准。

## 当前能力概览

- **数据计算**：从 shared CSV 输入生成结构化 JSON 数据包。
- **异常预警**：输出航线级价格、趋势、波动、预警等级和建议动作。
- **场景测算**：覆盖美西、美东等附加费 / 压力场景。
- **指数对比**：汇总 SCFI、CCFI、WCI、FBX、SCFIS、BDI、Brent 等外部指数信号。
- **决策输出**：生成发货节奏、观察窗口、风险解释和交叉验证结果。
- **Dashboard 展示**：`dashboard/demo-v3.html` 消费当前 output 数据结构。
- **本地一键验证**：`./scripts/smoke.sh` 运行完整 P0/P1 smoke tests。
- **远端 CI 验证**：GitHub Actions 在 push / pull request 时运行 smoke workflow。

## 目录结构

```text
.
├── dashboard/
│   └── demo-v3.html                 # Dashboard 页面
├── engine/
│   ├── compute.py                   # 从 shared 输入计算 output 五件套
│   ├── data_loader.py               # 数据加载工具
│   ├── metrics.py                   # 指标辅助逻辑
│   └── validate.py                  # output 数据包校验
├── output/
│   ├── metrics.json                 # 核心航线指标与预警结果
│   ├── history.json                 # 历史时间序列
│   ├── scenarios.json               # 场景测算结果
│   ├── decisions.json               # 决策建议与交叉验证
│   └── indices.json                 # 外部指数对比
├── scripts/
│   └── smoke.sh                     # 本地一键 smoke 验证脚本
├── tests/
│   ├── fixtures/shared/             # CI 可用的 shared 输入 fixture
│   ├── run_smoke_tests.py           # 统一 smoke 入口
│   ├── test_cli_paths.py            # CLI 路径回归
│   ├── test_validate_paths.py       # validate 路径回归
│   ├── test_output_smoke.py         # output 五件套契约校验
│   ├── test_compute_reproducibility.py
│   ├── test_compute_output_diff.py
│   └── test_dashboard_contract.py
└── .github/workflows/smoke.yml      # GitHub Actions smoke workflow
```

## output 五件套

当前交付数据包位于 `output/`：

| 文件 | 作用 |
|---|---|
| `metrics.json` | 航线核心指标、最新值、趋势、预警等级、建议动作 |
| `history.json` | 运价、指数、汇率等历史序列 |
| `scenarios.json` | 附加费和压力场景测算 |
| `decisions.json` | 发货建议、风险解释、交叉验证摘要 |
| `indices.json` | 外部指数对比和质量等级 |

这五个文件是 Dashboard 和后续分析的核心数据契约。

## 数据输入与 fixture

`engine/compute.py` 支持从 shared CSV 输入重新生成 `output` 五件套。

默认 CI / smoke tests 使用项目内 fixture：

```text
tests/fixtures/shared
```

这样远端 CI checkout 后即可运行，不依赖机器本地存在 `../shared`。

本地如需使用完整真实 shared 输入，可以通过环境变量覆盖：

```bash
CANGLU_SHARED_DIR=../shared ./scripts/smoke.sh
```

fixture 覆盖当前计算链路需要的数据源，包括但不限于：

- SCFI / CCFI / WCI / FBX / SCFIS
- BDI / Brent
- USD/CNY 汇率
- shipping events
- surcharge scenarios
- index comparison

如果后续正式 `output/` 更新，需要同步刷新 `tests/fixtures/shared`，否则数值 diff 测试会合理失败。

## 计算与校验

重新计算数据包：

```bash
python engine/compute.py --shared-dir tests/fixtures/shared --output-dir /tmp/canglu-output
```

校验某个 output 目录：

```bash
python engine/validate.py --data-dir output
```

说明：正式 smoke tests 会把 compute 输出写入临时目录，不会覆盖仓库中的正式 `output/`。

## Dashboard

Dashboard 文件：

```text
dashboard/demo-v3.html
```

当前测试已覆盖 Dashboard 字段契约，验证页面实际消费的字段可以从 `output` 五件套稳定映射出来，包括：

- `metrics.json -> routes`
- `history.json -> datasets`
- `scenarios.json -> scenarios`
- `decisions.json -> decisions`
- `indices.json -> indices`

已覆盖展示端短字段与正式字段之间的映射，例如：

- `val -> current_value/value`
- `z -> z_score`
- `wow -> wow_change_pct`
- `streak -> up_streak_weeks`
- `level -> warning_level`
- `advice -> suggestion`
- `ql -> quality_level`

当前 smoke tests 验证的是字段契约，不等同于真实浏览器渲染截图验收。

## 本地一键验证

推荐使用本地脚本：

```bash
./scripts/smoke.sh
```

等价直接命令：

```bash
python tests/run_smoke_tests.py
```

或在小浣熊环境中使用：

```bash
$BOX_AGENT_PYTHON tests/run_smoke_tests.py
```

通过时应看到：

```text
all P0/P1 smoke tests passed
```

当前统一 smoke tests 覆盖：

1. engine CLI 路径回归
2. validate 路径回归
3. output 五件套契约校验
4. compute 从 shared fixture 临时复算
5. 临时复算结果与正式 output 的数值容差 diff
6. Dashboard 字段契约校验

## GitHub Actions CI

远端 CI 配置文件：

```text
.github/workflows/smoke.yml
```

触发条件：

- push 到 `main`
- push 到 `master`
- pull request

CI 执行命令：

```bash
python tests/run_smoke_tests.py
```

当前 smoke workflow 已在 GitHub Actions 上实际运行通过，状态为 `completed / success`。

## 项目目录

```text
engine/                 计算、加载、指标和校验脚本
dashboard/              HTML Dashboard
output/                 当前正式五件套数据包
tests/                  smoke tests 与回归测试
tests/fixtures/shared/  CI 可用的 shared 输入 fixture
scripts/smoke.sh        本地一键验证脚本
.github/workflows/      GitHub Actions CI 配置
plans/                  审计、测试落地和治理文档
archive/                历史材料归档
```

## 当前已闭环能力

- 数据输入不再依赖机器外部 `../shared`。
- compute 可在临时目录复算五件套，不污染正式 `output/`。
- 复算结果可与正式 `output/` 做数值容差 diff。
- Dashboard 字段消费与五件套数据契约一致。
- 本地一键验证和 GitHub Actions CI 均已接入。
- P0/P1 smoke tests 已通过。

## 已知边界

- Dashboard smoke tests 当前覆盖字段契约，不覆盖真实浏览器渲染、截图和交互。
- `tests/fixtures/shared` 是当前正式 `output/` 对应输入快照；正式数据更新时需要同步刷新 fixture。
- 当前测试体系以轻量 smoke 为主，后续测试规模扩大后可迁移到 `pytest`。

## 背景说明

本项目最初来自一次比赛路演场景。比赛已经结束，相关材料已归档；当前 README 以项目现有功能、数据链路和验证体系为准。

更多审计和治理记录可见：

- `plans/final-audit-report.md`
- `plans/p0-test-landing-plan.md`
