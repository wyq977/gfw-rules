# Loon

Format and comments mainly based on [loon_diy](https://github.com/w37fhy/QuantumultX/blob/master/loon_diy.conf).

[Official manual, outdated, 2019-11-04](https://github.com/Loon0x00/LoonManual)

[Loon 不完全教程, Notion, 2020-05-23](https://www.notion.so/Loon-f0a98c39f5224c09b281c79837380431)

## Proxy

```conf
# not sure when to use this
[Proxy]
# 内置 DIRECT、REJECT 策略
# 节点名称 = 协议，服务器地址，服务器端口，加密协议，密码

# 机场订阅
[Remote Proxy]
# not sure if it's safe to upload to github
# subscription can be filter with Regex/keyword in [Remote Filter]
# 订阅节点，格式：别名 = 订阅 URL
# 以 Dler Cloud 为例，Dler Cloud 用户将下面订阅链接的 XXXXXX 替换为自己的订阅 token 即可
# 其他机场用户，注意修改别名（包括该配置文件下方所有 Dler Cloud 字样）
```

## 规则

```conf
[Rule]
# 本地规则部分书写在下面
# 格式为 **规则类型,域名(部分类型可省略),策略**
#             
# 目前支持的类型有      
# DOMAIN-SUFFIX  基于域名后缀
# DOMAIN         基于域名完整匹配
# DOMAIN-KEYWORD 基于域名关键字
# USER-AGENT     基于用户代理串
# URL-REGEX      基于 URL 正则
# IP-CIDR        基于请求 IP 范围
# GEOIP          基于 IP 定位国家编码
# FINAL          兜底策略，所有策略都未匹配上时使用
#
# 目前支持的策略有
# DIRECT 直连，即所有流量不通过代理，在国内就走国内IP，在国外就走国外IP
# Proxy  策略组名, 这里可自定义名字，名字值为 [Proxy Group] 或者 [Proxy] 中的自定的值
# REJECT 拒绝策略，通常用作去广告
#
# 可选项:force-remote-dns(Default:false),no-resolve
DOMAIN,google.com,PROXY
# GeoIP 为中国的，走直连
GEOIP,CN,DIRECT
# 兜底策略使用 Final 策略组
FINAL,Final

[Remote Rule]
# 远程规则部分书写在下面
# 格式为 订阅规则 URL**,策略**

# 如以下地址将使用，PROXY 这个策略组
https://raw.githubusercontent.com/Loon0x00/LoonExampleConfig/master/Rule/ExampleRule.list,PROXY
```

## 策略组

[关于策略组的理解](https://github.com/Fndroid/jsbox_script/wiki/%E5%85%B3%E4%BA%8E%E7%AD%96%E7%95%A5%E7%BB%84%E7%9A%84%E7%90%86%E8%A7%A3)

```conf
[Proxy Group]
# [select] 手动选择
# 在节点列表手动选择一个节点或策略组
PROXY = select,Auto,1,2,3,4,Subs

# [url-test] 延迟测试
# 给提供的url发出http header请求，根据返回结果，选择测速最快的节点，
# 默认间隔600s，测速超时时间5s，为了避免资源浪费，建议节点数不要过多，
# 只支持单个节点和远端节点，其他会被忽略
# 不支持嵌套策略组
Auto = url-test,1,2,3,4,Subs,url = http://bing.com/,interval = 600

# [fallback] 可用测试
# 和url-test类似，不同的是会根据顺序返回第一个可用的节点，为了避免资源浪费，
# 建议节点数不要过多，只支持单个节点和远端节点，其他会被忽略
Auto1 = fallback,1,2,3,4,Subs,url = http://bing.com/,interval = 600

# [ssid] 网络类型
# 根据网络类型或路由器名称选择节点或策略组
# 别名 = ssid，默认 = 策略， 蜂窝 = 策略， ssid名称 = 策略
SSID = ssid, default = PROXY, cellular = DIRECT, "DivineEngine" = PROXY

# [load-balance] 负载均衡
# 可选三种算法
# random：随机选择策略组可用节点
# round-robin：轮询策略组可用节点
# pcc：在random基础上，针对相同host使用同一节点，此处url用来测试节点可用性
# 每隔interval进行一次测速，max-timeout参数用于筛选测试时间超过max-timeout的节点为不可用节点
LoadBalance = load-balance,node1,node2,remoteNodes, url = http://bing.com, interval = 600,algorithm = pcc, max-timeout = 3000

# [REJECT] 拒绝
# 阻止请求进行 通常用作去广告
# Advertising = select,REJECT,DIRECT

# [DIRECT] 直连
# 不进行代理
# 即所有流量不通过代理，在国内就走国内IP(不出国)，在国外就走国外IP(不回国)
# Final = select,PROXY,DIRECT
```

## URL Rewrite Mitm

### 重写原理

在 Loon 接收到 HTTP 请求时，会使用请求的 url 去寻找有没有匹配的 `url rewrite` 规则，若满足规则，会替换或修改 HTTP 请求中的 url 或替换请求响应体

### 重写格式

正则表达式, 替换内容, 重写类型

如 `https?://(www.)?g.cn https://www.google.com 302`

表示匹配到 [g.cn](http://g.cn) 或者 [www.g.cn](http://www.g.cn) 会 302 重定向到 https://www.google.com

[重写规则](https://www.notion.so/b71021ef7be84c47a818d04c23266af6)

### MITM 解密

中间人攻击方式可以来解密 https 的请求。Loon会根据配置的 hostname 和信任的CA证书解密相应的 https 请求和响应，解密后可以配合 Rule 和 URL Rewrite 进行分流。

## Ref

https://github.com/w37fhy/QuantumultX/blob/master/loon_diy.conf
https://github.com/zqzess/rule_for_quantumultX/blob/master/Loon/zqzess_Loon.conf
https://github.com/blackmatrix7/ios_rule_script
https://github.com/sve1r/Rules-For-Quantumult-X
https://github.com/Arron-CN/Rule/blob/master/Loon/Loon.conf
https://github.com/Tartarus2014/Loon-Script/blob/master/Loon_tf_cn.conf