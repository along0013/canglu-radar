# 截图+OCR周度补采计划

## 目标

在不等待官方API的情况下，以人工截图+OCR方式补齐缺失周次，并统一标注为 `B_screenshot_ocr`，不得升级为A类。

## SCFI

- 来源候选：上海航交所、维运网、新浪财经等公开页面。
- 每周动作：截图保存、OCR读取日期/指数/航线价格、人工抽样复核。
- 输出字段：date、natural_week_start、index_type、route_name、value、unit、data_quality_level、evidence_file、review_status。
- 质量等级：`B_screenshot_ocr`；无法复核则 `PENDING`。

## USD/CNY汇率

- 延续已验证截图OCR策略。
- 取自然周最后可见交易日代表值。
- 表头不可见或字段推定时保持 `B_screenshot_ocr`，不标A。

## 船司公告

- 来源候选：Maersk、MSC、COSCO、CMA CGM等官网公告页。
- 每周保存公告截图/PDF，提取carrier、announcement_date、effective_date、route_scope、amount、currency、event_type。
- 质量等级：公开官网截图为 `B_screenshot_ocr`，字段缺失为 `PENDING`。

## 复核机制

- 每批至少抽查20%记录。
- 检查日期、金额、单位、航线是否一致。
- OCR不确定字段不得补猜，统一填PENDING。
