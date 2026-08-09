# 舱路雷达｜数据采集网站清单与注册判断

> 用途：供用户在小浣熊另一个对话框/专属浏览器中逐一打开网站，手动查询、复制或下载数据。  
> 策略：优先不注册、免费公开页面、单期查询、二手新闻/财经平台；仅在确实无法替代时考虑注册或付费。

---

## 0. 推荐采集顺序

1. **上海航运交易所单期查询 SCFI**：逐周查询近26周，不用多期查询，尽量避开付费注册。
2. **东方财富 / 新浪财经 / 同花顺 / 国际船舶网**：补充每周 SCFI 报道，尤其是历史周数据。
3. **中国货币网 / 国家外汇管理局 / 中国经济网**：采 USD/CNY 中间价。
4. **Maersk / MSC / COSCO / ONE / Evergreen 官网**：采船司公告；官网拿不到就用行业转载文本。
5. **东方财富 / 新浪财经 / FRED / EIA / 生意社**：采布伦特油价或燃油价格背景。

---

## 1. 航运指数类网站

| 优先级 | 网站名称 | 网址 | 需要内容 | 是否必须注册 | 是否可能付费 | 建议操作 |
|---|---|---|---|---|---|---|
| 高 | 上海航运交易所 SCFI 单期查询 | https://www.sse.net.cn/index/singleIndex?indexType=scfi | SCFI 单期数据：综合指数、欧洲、地中海、美西、美东 | **通常不需要** | 否 | 按周五日期逐期查询，复制表格；用于近26周手工补齐 |
| 高 | 上海航运交易所 SCFI 多期查询 | https://www.sse.net.cn/index/scfilist | SCFI 近26周批量数据 | 需要登录 | **可能需要会员/付费权限** | 不作为主路径；如已确认付费，则跳过 |
| 中 | 上海航运交易所 CCFI 单期查询 | https://www.sse.net.cn/index/singleIndex?indexType=ccfi | CCFI 单期数据：综合、美西、美东、欧洲、地中海、日本等 | 通常不需要 | 否 | 可逐周采集，用于交叉验证，不阻塞主流程 |
| 中 | 上海航运交易所 SCFIS 单期查询 | https://www.sse.net.cn/index/singleIndex?indexType=scfis | SCFIS 单期结算价：欧洲、美西等 | 通常不需要 | 否 | 近12周逐期采，作为增强项 |
| 中 | 上海航运交易所官网首页/指数栏目 | https://www.sse.net.cn/ | 指数入口、公告、单期页面跳转 | 不需要 | 否/部分功能可能需要会员 | 找不到入口时从首页进入“运价指数” |

### 1.1 SCFI 近26周逐周单期查询方法

如果多期查询需要付费注册，就改用单期查询。

操作方式：

1. 打开：`https://www.sse.net.cn/index/singleIndex?indexType=scfi`
2. 在日期框输入一个周五日期。
3. 查询后复制表格中的：
   - 发布日期
   - 综合指数
   - 欧洲航线
   - 地中海航线
   - 美西航线
   - 美东航线
4. 重复近26个周五。
5. 可以先复制到 Excel，再上传给小浣熊清洗。

建议字段：

```text
date, scfi_composite, europe_usd_teu, mediterranean_usd_teu, us_west_usd_teu, us_east_usd_teu, source_url, data_quality_level, note
```

建议近26周日期可以先按周五倒推；若某周五无数据，则尝试周六或官网发布日。

---

## 2. 二手财经/航运新闻平台：用于补 SCFI 历史周数据

| 优先级 | 网站名称 | 网址 | 需要内容 | 是否必须注册 | 是否可能付费 | 建议搜索关键词 |
|---|---|---|---|---|---|---|
| 高 | 东方财富 | https://www.eastmoney.com/ | 每周 SCFI 报道、航运指数、船公司公告转载、油价新闻 | 通常不需要 | 否 | `SCFI 上海航运交易所 美西 美东 欧洲 地中海 2026` |
| 高 | 东方财富财富号 | https://caifuhao.eastmoney.com/ | 行业号转载的 SCFI 周报、船司公告 | 通常不需要 | 否 | `SCFI 2026 5月 上海航交所 运价指数` |
| 高 | 新浪财经 | https://finance.sina.com.cn/ | 航运、油价、汇率、期货资讯 | 通常不需要 | 否 | `SCFI 运价指数 欧洲 美西 美东`、`布伦特原油 历史行情` |
| 高 | 同花顺财经 | https://www.10jqka.com.cn/ | SCFI/CCFI周报转载、航运市场报道 | 通常不需要 | 否 | `SCFI 上海航交所 2026 03 20` |
| 高 | 国际船舶网 | http://www.eworldship.com/ | 每周 SCFI、航运市场资讯、船公司动态 | 通常不需要 | 否 | `SCFI 运价指数 2026 美西 美东 欧洲` |
| 中 | 航运界 | https://www.ship.sh/ | 航运市场周报、船公司公告转载 | 可能需要登录/部分内容限制 | 可能有会员内容 | `SCFI 周报 美西 欧洲` |
| 中 | 港口网 | https://www.chinaports.com/ | 港口、航运、指数报道 | 可能需要注册 | 可能有会员内容 | `上海出口集装箱运价指数 SCFI` |
| 中 | 中国水运网 | https://www.zgsyb.com/ | 航运市场新闻、政策、港口背景 | 通常不需要 | 否/部分内容可能限制 | `SCFI 运价指数` |
| 中 | 中国船东协会 | http://www.csoa.cn/ | 船司公告转载、行业动态 | 通常不需要 | 否 | `MSC 停航 马士基 绕航 公告` |

### 2.1 二手平台采集建议

如果在上海航运交易所单期查询某一周失败，可以在搜索引擎或站内搜索：

```text
SCFI 2026-05-15 上海航运交易所 美西 美东 欧洲 地中海
SCFI 5月15日 上海航交所 运价指数
上海出口集装箱运价指数 2026 05 15
```

保存时需要保留：

```text
source_url
source_name
publish_date
data_quality_level = B
note = 公开转载数据，需与官方口径核验
```

---

## 3. 汇率数据网站

| 优先级 | 网站名称 | 网址 | 需要内容 | 是否必须注册 | 是否可能付费 | 建议操作 |
|---|---|---|---|---|---|---|
| 高 | 中国货币网 / 中国外汇交易中心 | https://www.chinamoney.com.cn/ | USD/CNY 人民币汇率中间价，近26周周五或最近交易日 | 通常不需要，但页面复杂/可能有验证码 | 否 | 搜索“人民币汇率中间价”，按日期查询并复制 |
| 高 | 国家外汇管理局 | https://www.safe.gov.cn/ | 人民币汇率中间价或外汇统计数据 | 通常不需要 | 否 | 查历史统计/汇率栏目 |
| 高 | 中国经济网 | http://www.ce.cn/ | 每日人民币汇率中间价新闻 | 不需要 | 否 | 搜索 `人民币汇率中间价 2026-05-15` |
| 中 | 东方财富外汇行情 | https://quote.eastmoney.com/ | USD/CNY 市场汇率代理 | 通常不需要 | 否 | 搜索“美元人民币”或 `USDCNY` |
| 中 | 新浪财经外汇 | https://finance.sina.com.cn/money/forex/ | USD/CNY 市场行情 | 通常不需要 | 否 | 搜索“美元人民币 历史行情” |
| 中 | Investing 英为财情 | https://cn.investing.com/ | USD/CNY 历史数据 | 可能需要免费注册/弹窗 | 高级功能可能付费 | 免费注册可考虑；若要求付费则跳过 |
| 中 | Yahoo Finance | https://finance.yahoo.com/quote/CNY=X/ | USD/CNY 市场汇率 | 不一定需要 | 否/部分限制 | 可能受地区/反爬影响 |
| 中 | Stooq | https://stooq.com/ | USD/CNY 历史CSV | 不需要 | 否 | 若可访问，适合导出CSV |

### 3.1 汇率替代口径

优先使用官方中间价。若拿不到，可使用市场汇率代理，但必须标注：

```text
rate_type = market_proxy
data_quality_level = B
note = 非中国外汇交易中心官方中间价，仅作为趋势代理
```

---

## 4. 船公司官网与公告平台

| 优先级 | 网站名称 | 网址 | 需要内容 | 是否必须注册 | 是否可能付费 | 建议搜索关键词 |
|---|---|---|---|---|---|---|
| 高 | Maersk 马士基 | https://www.maersk.com.cn/news/articles | GRI、PSS、BAF/LSS、停航、绕航、港口拥堵 | 通常不需要 | 否 | `PSS Far East Asia`、`surcharge Europe`、`blank sailing` |
| 高 | MSC | https://www.msc.com/ | 停航、跳港、拥堵、附加费公告 | 通常不需要，但页面地区跳转复杂 | 否 | `blank sailing`、`port omission`、`congestion`、`customer advisory` |
| 高 | COSCO 中远海运 | https://lines.coscoshipping.com/ | PSS、GRI、客户通知 | 可能需要选择地区/语言 | 通常否 | `PSS`、`Peak Season Surcharge`、`Rate Announcement` |
| 高 | ONE 海洋网联 | https://www.one-line.com/ | BAF、LSS、PSS、客户通知 | 通常不需要 | 否 | `BAF`、`Bunker Adjustment Factor`、`Low Sulphur Surcharge` |
| 中 | Evergreen 长荣 | https://www.evergreen-line.com/ | 停航、跳港、港口拥堵、附加费 | 可能需要选择地区 | 通常否 | `blank sailing`、`port omission`、`surcharge` |
| 中 | Hapag-Lloyd | https://www.hapag-lloyd.com/ | 附加费、PSS、GRI、运营公告 | 通常不需要，部分客户功能需登录 | 否/客户功能可能需账号 | `tariff`, `surcharge`, `PSS`, `GRI` |
| 中 | CMA CGM | https://www.cma-cgm.com/ | 附加费公告、PSS、GRI | 通常不需要 | 否 | `PSS`, `GRI`, `surcharge`, `Asia Europe` |

### 4.1 船司公告采集格式

如果官网有 PDF，下载 PDF。  
如果只有网页，复制正文保存为 `.txt` 或打印为 PDF。

建议字段：

```text
carrier
event_type
announcement_title
publish_date
effective_date
expiry_date
route_text
route_code
amount
currency
container_type
source_url
source_type
data_quality_level
```

### 4.2 需要找的 5 类公告

| 类型 | 英文关键词 | 至少需要几份 |
|---|---|---|
| 停航/空班 | `blank sailing`, `void sailing`, `service suspension` | 1 |
| GRI | `General Rate Increase`, `rate restoration`, `rate increase` | 1 |
| PSS | `Peak Season Surcharge` | 1 |
| BAF/LSS | `Bunker Adjustment Factor`, `Low Sulphur Surcharge`, `fuel surcharge` | 1 |
| 跳港/港口拥堵 | `port omission`, `congestion`, `port rotation change` | 1 |

---

## 5. 油价与燃油背景数据

| 优先级 | 网站名称 | 网址 | 需要内容 | 是否必须注册 | 是否可能付费 | 建议操作 |
|---|---|---|---|---|---|---|
| 高 | 东方财富行情中心 | https://quote.eastmoney.com/ | 布伦特原油历史行情 | 通常不需要 | 否 | 搜索“布伦特原油” |
| 高 | 新浪财经期货 | https://finance.sina.com.cn/futures/ | 布伦特原油、原油期货行情 | 通常不需要 | 否 | 搜索“布伦特原油 历史行情” |
| 中 | 生意社 | https://www.100ppi.com/ | 原油、燃油价格走势 | 通常不需要 | 否/部分数据可能会员 | 搜索“布伦特原油 价格走势” |
| 中 | FRED | https://fred.stlouisfed.org/series/WCOILBRENTEU | Brent 周度价格 | 不需要 | 否 | 如能访问，可下载CSV |
| 中 | EIA | https://www.eia.gov/ | 国际油价数据 | 不需要 | 否 | 数据较权威，但页面较复杂 |
| 中 | Investing 英为财情 | https://cn.investing.com/commodities/brent-oil-historical-data | Brent 历史数据 | 可能免费注册 | 高级功能可能付费 | 免费注册可考虑，付费则跳过 |

---

## 6. 哪些网站值得注册？

| 网站 | 是否建议注册 | 原因 |
|---|---|---|
| 上海航运交易所 | **不建议付费注册** | 多期查询可能需会员/企业付费；单期查询可替代，二手平台可补充 |
| Investing 英为财情 | 可免费注册，但不建议付费 | 免费注册可能解除部分下载限制；付费价值不高 |
| 航运界/港口网 | 可视情况免费注册 | 如果注册后能看历史报道，可考虑；付费会员不建议 |
| 船司官网 | 一般不需要注册 | 新闻/公告多数公开，客户系统才需登录 |
| 东方财富/新浪财经/同花顺 | 一般不需要注册 | 新闻和行情通常公开可看 |
| 中国货币网/国家外汇管理局 | 一般不需要注册 | 官方公开数据，主要是页面复杂或验证码问题 |

---

## 7. 最小手工采集包

如果时间有限，建议你只采这些：

| 数据 | 最小数量 | 来源建议 |
|---|---:|---|
| SCFI | 近26周，每周1条 | 上海航交所单期查询 + 东方财富/同花顺/国际船舶网补缺 |
| USD/CNY | 近26周，每周1条 | 中国货币网/中国经济网/东方财富代理 |
| 船司公告 | 5类各1份 | Maersk、MSC、COSCO、ONE、Evergreen 官网或转载 |
| 附加费规则 | 1份 | 模拟样例数据 |
| 航线字典 | 1份 | 自行整理 |

---

## 8. 复制给小浣熊的数据格式建议

### SCFI 粘贴格式

```text
发布日期 综合指数 欧洲航线 地中海航线 美西航线 美东航线 来源URL
2026-05-15 2140.66 1816 2345 3118 4224 http://xxx
```

### 汇率粘贴格式

```text
日期 USD/CNY 来源URL
2026-05-15 7.2000 http://xxx
```

### 公告粘贴格式

```text
公告类型：PSS
船公司：Maersk
标题：xxx
发布日期：2026-03-12
生效日期：2026-03-17
金额：USD 500 / container
航线：Far East Asia to India/Nepal
来源URL：https://xxx
正文：...
```

---

## 9. 结论

- **上海航运交易所多期查询**：若已确认付费注册，不作为主路径。
- **上海航运交易所单期查询**：优先使用，逐周采集近26周，可绕开多期付费限制。
- **东方财富、同花顺、国际船舶网、新浪财经**：用于补历史周数据和来源交叉验证。
- **船司官网**：优先拿公告网页/PDF；拿不到官方原文时用行业转载并标注。
- **注册策略**：免费注册可以考虑；付费注册不建议，除非后续项目进入正式商业化阶段。
