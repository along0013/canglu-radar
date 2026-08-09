# canglu-radar 最终审计报告

## 1. 审计结论

当前项目已经完成 P0 主链路闭环：

```text
shared 原始输入
  -> engine/compute.py 复算 output 五件套
  -> engine/validate.py 校验 output 五件套
  -> tests 输出契约 smoke test
  -> dashboard/demo-v3.html 字段契约 smoke test
```

统一验证入口已形成：

```bash
$BOX_AGENT_PYTHON tests/run_smoke_tests.py
```

最近一次验证结果：

```text
engine CLI path regression tests passed
validate path regression tests passed
output package smoke tests passed
compute reproducibility smoke test passed
dashboard field contract tests passed
all P0 smoke tests passed
```

## 2. P0：已闭环可信链路

### P0-1 CLI 路径入口可信

已覆盖文件：

- `engine/validate.py`
- `engine/compute.py`
- `tests/test_cli_paths.py`
- `tests/test_validate_paths.py`

可信结论：

- `engine/validate.py --data-dir output` 已能从项目根目录正确解析到 `output/`。
- `engine/compute.py --shared-dir ... --output-dir ...` 已统一走 CLI 路径解析逻辑。
- 相对路径、绝对路径和缺失路径 fallback 行为均有回归测试。

验证命令：

```bash
$BOX_AGENT_PYTHON tests/test_cli_paths.py
$BOX_AGENT_PYTHON tests/test_validate_paths.py
```

### P0-2 output 五件套契约可信

已覆盖文件：

- `output/metrics.json`
- `output/history.json`
- `output/scenarios.json`
- `output/decisions.json`
- `output/indices.json`
- `tests/test_output_smoke.py`

可信结论：

- 五件套文件存在且 JSON 可解析。
- `_meta.version/latest_week/fx_rate` 在五件套中保持一致。
- 核心 section 非空。
- `metrics`、`history`、`decisions` 的航线集合一致。
- `scenarios` 覆盖当前项目设计中的 `USWC/USEC` 场景。

验证命令：

```bash
$BOX_AGENT_PYTHON tests/test_output_smoke.py
$BOX_AGENT_PYTHON engine/validate.py --data-dir output
```

### P0-3 compute 从 shared 复算可信

已覆盖文件：

- `engine/compute.py`
- `../shared/*.csv`
- `tests/test_compute_reproducibility.py`

可信结论：

- 可从真实 `../shared` 输入复算 output 五件套。
- 复算输出写入临时目录，不覆盖正式 `output/`。
- 临时五件套通过结构契约检查。
- 临时五件套可继续通过 `engine/validate.py` 校验。

验证命令：

```bash
$BOX_AGENT_PYTHON tests/test_compute_reproducibility.py
```

### P0-4 Dashboard 字段契约可信

已覆盖文件：

- `dashboard/demo-v3.html`
- `output/*.json`
- `tests/test_dashboard_contract.py`

可信结论：

- Dashboard 实际消费的核心字段，在 output 五件套中均有对应来源字段。
- 已覆盖 Dashboard 简写字段与 output 正式字段映射，例如：
  - `val -> current_value/value`
  - `z -> z_score`
  - `wow -> wow_change_pct`
  - `streak -> up_streak_weeks`
  - `level -> warning_level`
  - `advice -> suggestion`
  - `ql -> quality_level`
- Dashboard 嵌入快照的航线、场景和指数覆盖范围与 output 当前契约一致。

验证命令：

```bash
$BOX_AGENT_PYTHON tests/test_dashboard_contract.py
```

### P0-5 一键回归入口可信

已覆盖文件：

- `tests/run_smoke_tests.py`

可信结论：

- 一条命令可以验证当前 P0 主链路。
- 适合作为后续修改 `engine/`、`output/`、`dashboard/` 前后的最低回归门禁。

验证命令：

```bash
$BOX_AGENT_PYTHON tests/run_smoke_tests.py
```

## 3. P1：剩余风险与建议

### P1-1 缺少浏览器真实渲染验证

风险：

- 当前 Dashboard 测试是静态字段契约测试。
- 不能证明图表、交互、响应式布局在浏览器中真实可用。

建议下一步：

- 在具备 Playwright 或浏览器连接器后，补充 Dashboard smoke render test：
  - 页面打开无 JS error。
  - 核心卡片数量正确。
  - tabs 可切换。
  - route / scenario / index 渲染节点存在。

### P1-2 compute 仅验证结构可复算，未做语义级 diff

风险：

- 当前复算测试验证的是临时五件套结构与 validate 契约。
- 没有与正式 `output/` 做字段级或数值容差 diff。

建议下一步：

- 增加 `tests/test_compute_output_diff.py`：
  - 对复算输出与正式 output 做核心字段比较。
  - 对浮点值使用合理 tolerance。
  - 对说明性文本、生成时间类字段避免硬比较。

### P1-3 shared 输入目录仍在项目外部

风险：

- `../shared` 是项目外部相邻目录。
- 如果迁移仓库或交付给第三方，compute 复算会因输入缺失失败。

建议下一步：

- 在 README 中明确 `../shared` 前置条件。
- 或提供 `shared/manifest` 与样例数据包说明。

## 4. P2：治理与工程化建议

### P2-1 接入 CI

建议：

- 若后续进入持续维护阶段，把以下命令接入 CI：

```bash
$BOX_AGENT_PYTHON tests/run_smoke_tests.py
```

### P2-2 引入 pytest 但不作为当前阻塞

建议：

- 当前标准库脚本式测试已经满足 P0。
- 若测试规模继续增加，可迁移到 pytest，提高断言报告可读性。

### P2-3 文档化数据版本与字段映射

建议：

- 将 Dashboard 简写字段与 output 正式字段映射固化到 specs 或 README。
- 避免未来仅改 output 字段导致 Dashboard 静态快照断裂。

## 5. 建议下一步执行顺序

已立即执行的动作：

1. 生成本最终审计报告。
2. 将统一 P0 验证入口写入 README。
3. 再次运行 `tests/run_smoke_tests.py` 做最终回归。

后续建议顺序：

1. P1：补 compute 复算结果与正式 output 的字段级/数值容差 diff。
2. P1：在浏览器能力可用时补 Dashboard render smoke test。
3. P2：接入 CI 或交付前检查脚本。

## 6. 当前状态

当前项目已经具备 P0 级可信链路：

```text
路径入口可信 + output 数据可信 + compute 可复算 + Dashboard 字段契约可信 + 一键验证入口可信
```
