# 2026年5月底附加费参考行情接入说明

## 来源
- 用户提供文本：`output/附加费明细.txt`
- 内容说明：海运附加费完整一览表，覆盖 BAF、PSS、THC、拥堵费、EBS、GRI、CIC、WRS、PCS、LSS、DOC、SEAL、AMS/ENS、设备交接单费等项目。

## 数据层级
- `data_quality_level = C_market_reference`
- 原因：该表为用户提供的市场行情参考文本，未附船司官网公告、合同价、报价单或业务系统导出的脱敏费率明细。
- 可用于：演示测算、参数占位、敏感性分析、成本模型初版。
- 不可用于：A/B层真实费率结论、正式对外报价、合同级成本核算。

## 已生成文件
- `surcharge-market-reference-2026-05.csv`：完整结构化参考行情。
- `surcharge-cost-model-reference-input-2026-05.csv`：成本模型可调用字段，默认使用区间中位数作为演示值。
- `原始_附加费规则.xlsx`：已新增/替换 `2026_market_reference` 工作表，原模拟样例工作表保留。

## 成本测算调用建议
1. 若为演示版成本测算，可读取 `surcharge-cost-model-reference-input-2026-05.csv`。
2. 对 `unit = USD/FEU` 的费用，可按每40尺柜直接计入。
3. 对 `USD/shipment` 的费用，应按每票计入，并根据票柜比拆分至单柜。
4. 对 `USD/container` 的费用，应按每柜计入。
5. 对 `included_in_BAF` 的费用，不再重复计入，避免双算。
6. 正式测算前，需要使用合同价/船司公告/报价单替换 C 级参考值。
