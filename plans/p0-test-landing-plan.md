# canglu-radar P0 测试落地计划

## 1. 当前目标

把项目从“封存展示包”推进到“关键数据包可验证、核心入口可复跑、路径行为不误导”的 P0 稳定状态。

最初方向不是做复杂 Web 自动化，也不是大规模重构，而是完成本地现状审计后，优先落地最小可信测试闭环：

1. `validate.py` 能稳定校验 `output/` 五件套。
2. `output/*.json` 的结构和跨文件一致性有 smoke test 兜底。
3. CLI 相对路径行为符合项目根目录执行习惯。
4. 后续再推进 `compute.py` 原始输入复算和 Dashboard 字段契约测试。

## 2. 已完成修复

### 2.1 `engine/validate.py` 路径解析修复

已修复：

```bash
$BOX_AGENT_PYTHON engine/validate.py --data-dir output
```

此前 `output` 会被误解析为 `engine/output`；现在优先按当前工作目录解析，若不存在再兼容脚本目录相对路径。

### 2.2 `engine/compute.py` CLI 路径隐患修复

已同步修复：

- `--shared-dir`
- `--output-dir`
- 位置参数 shared 路径

相对路径优先按当前工作目录解析；必要时兼容历史脚本目录 fallback。

### 2.3 新增测试入口

已新增统一 P0 smoke 测试入口：

```bash
$BOX_AGENT_PYTHON tests/run_smoke_tests.py
```

当前纳入：

- `tests/test_cli_paths.py`
- `tests/test_validate_paths.py`
- `tests/test_output_smoke.py`

## 3. output 五件套 smoke test 范围

新增文件：

```text
tests/test_output_smoke.py
```

覆盖对象：

- `output/metrics.json`
- `output/history.json`
- `output/scenarios.json`
- `output/decisions.json`
- `output/indices.json`

覆盖断言：

1. 五个 JSON 文件均存在且可解析。
2. 每个文件均包含 `_meta`。
3. `_meta.version` 为 `5.0`。
4. `_meta.latest_week` 非空。
5. `_meta.fx_rate` 为数值。
6. 五件套的 `latest_week` 一致。
7. 五件套的 `fx_rate` 一致。
8. `metrics.json` 与 `decisions.json` 的航线集合一致。
9. `history.json` 覆盖 `EUR / MED / USWC / USEC / COMPOSITE`。
10. `scenarios.json` 覆盖 `USWC / USEC`。
11. 通过子进程调用 `validate.py --data-dir output`，验证 CLI 相对路径与完整校验链路。

## 4. 本轮验证结果

执行命令：

```bash
cd /Users/along/小浣熊/canglu-radar
$BOX_AGENT_PYTHON tests/run_smoke_tests.py
$BOX_AGENT_PYTHON engine/validate.py --data-dir output
```

结果：

```text
engine CLI path regression tests passed
validate path regression tests passed
output package smoke tests passed
all P0 smoke tests passed

validate.py:
ERROR:   0
WARNING: 0
全部通过 — 数据一致性无异常
```

结论：

- `validate.py / output 五件套` 的正式 P0 smoke test 已补齐。
- 已接入当前项目的统一轻量测试入口。
- `engine/validate.py --data-dir output` 已作为回归项被测试覆盖。

## 5. 近期迭代方向校准

这几轮修复没有偏离主线，但需要收敛边界：

### 继续坚持的方向

P0 主线仍是：

```text
数据包可信 → 路径入口可信 → 计算链路可复跑 → Dashboard 字段契约可信
```

当前已完成前两项，并补上了 `output 五件套` 的 smoke test。

### 需要避免的发散

暂不建议优先投入：

- 复杂 UI 自动化。
- PPT / archive 展示材料重做。
- 大规模 pytest / CI 改造。
- 重构业务指标计算逻辑。
- 调整 `output/` 既有数据内容。

### 下一步建议调整

原本下一步可直接做 Dashboard 字段契约测试；但从 P0 风险链来看，更合理的顺序是：

1. 先确认 `compute.py` 是否能从真实 shared 输入复算出五件套。
2. 如果 shared 输入缺失，先在文档中明确“复算阻塞点”，并补一个缺失输入时的友好失败测试。
3. 再补 Dashboard 字段契约测试，确保前端消费的是当前五件套真实字段。

原因：Dashboard 只是展示层；如果计算链路不可复跑，P0 的根因链仍不完整。

## 6. 当前文件清单

已改动/新增：

```text
engine/validate.py
engine/compute.py
tests/test_cli_paths.py
tests/test_validate_paths.py
tests/test_output_smoke.py
tests/run_smoke_tests.py
plans/p0-test-landing-plan.md
```

## 7. 当前 caveat

1. 当前 smoke test 证明的是 `output/` 数据包契约和 `validate.py` 校验入口可信。
2. 还不能证明 `compute.py` 可以在本机从原始 shared 输入完整复算，因为真实 shared 输入目录仍需确认。
3. 当前测试入口是标准库脚本式 runner，没有引入 pytest；这符合项目现状，也减少前期依赖复杂度。
4. Dashboard 字段契约测试尚未落地，应在 compute 复跑链路确认后补齐。

## 8. 推荐下一步

下一步 P0 工作建议：

```bash
$BOX_AGENT_PYTHON engine/compute.py --shared-dir <真实 shared 输入目录> --output-dir /tmp/canglu-radar-output-check
$BOX_AGENT_PYTHON engine/validate.py --data-dir /tmp/canglu-radar-output-check
```

若真实 shared 输入目录不存在，则先补：

- `compute.py` 缺失输入的友好错误提示；
- 对该错误提示的回归测试；
- README / plans 中的复跑前置条件说明。
