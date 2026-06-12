# 舱路雷达｜命名与字段规范

## 文件命名

统一格式：

```text
CR-批次号_模块_描述.扩展名
```

示例：

- CR-02A_字段字典.xlsx
- CR-04A_指标计算结果.xlsx
- CR-05_分析报告.docx

## 数据列名规范

| 列名 | 含义 |
|---|---|
| date | 日期 |
| route_code | 航线代码 |
| route_name | 航线中文 |
| freight_usd | 运价/费用美元值 |
| unit | 单位 |
| fee_type | 费用类型 |
| carrier | 船公司 |
| usd_cny_rate | 汇率 |
| data_source | 数据来源 |

## 航线代码

- CN-USWC：中国-美西
- CN-USEC：中国-美东
- CN-EUR：中国-欧洲
