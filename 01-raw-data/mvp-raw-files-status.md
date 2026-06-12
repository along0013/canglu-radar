# 舱路雷达 MVP 原始文件采集状态

## 已落地文件

1. freight-index/原始_SCFI运价指数.csv
2. exchange-rate/原始_汇率.csv
3. carrier-announcements/原始_船公司公告_GRI_马士基.pdf
4. carrier-announcements/原始_船公司公告_PSS_中远.pdf
5. carrier-announcements/原始_船公司公告_BAF_ONE.pdf
6. carrier-announcements/原始_船公司公告_停航_MSC.pdf
7. surcharge-rules/原始_附加费规则.xlsx

## 注意

- SCFI 已填入公开转载可核验的5个周度点，其余周标记 pending_collection。
- 汇率当前为 MVP 模拟序列，必须由网桥替换为官方或行情源真实数据后用于正式结论。
- PSS/BAF/停航公告中部分目标船司未直接定位到稳定PDF，已使用可追溯公开网页快照/候选来源生成 PDF，以保证解析工作流可跑通。
- 附加费规则表为显式模拟数据，字段与工作流对齐。
