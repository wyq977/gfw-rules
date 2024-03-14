# 分流

* [【小白教程】10分钟搞懂分流策略 | 分流规则、策略组详解，如何DIY自己的专属分流策略，新手避坑指南！](https://w37fhy.com/archives/776)


## sve1r/Rules-For-Quantumult-X 推荐

* [推荐排序](https://github.com/sve1r/Rules-For-Quantumult-X#3%E6%8E%A8%E8%8D%90%E6%8E%92%E5%BA%8F)

Plugin __高于__ 分流

```
Advertising # only on iOS
Hijacking   # only on iOS
    Youtube.list
    Netflix.list
ForeignMedia.list - 国际流媒体
Apple.list - Apple 服务（可不加）# Apple 优先级高一点
Global.list - 国际网站/应用
China.list 
```

* 如若不需要观看哔哩哔哩、爱奇艺面向港澳台的限定内容可不加「DomesticMedia.list」。
* 如若不需要代理 Apple 服务可不加「Apple.list」，若加入必须在「Global.list」和「China.list」之间。
* 如需细化流媒体如「YouTube.list」需要加在「ForeignMedia.list」之前。
* 如需应用类的如「Telegram.list、Google.list、PayPal.list」需要加在「Global.list」之前。


## dunlanl/FuGfConfig 推荐

* [Apple分流规则](https://github.com/Elysian-Realme/FuGfConfig?tab=readme-ov-file#对于-apple-分流规则) 


对于本项目

AppleRules 是与本地化息息相关的规则，比如地图、天气、查找、Facetime、Apple Pay ( iCloud 上传与下载也归于此规则集

AppleCDNRules 是苹果的全球 CDN

AppleNoChinaCDNRules 是大陆没有的 CDN 节点

AppleAPIRules 是苹果的 API 域名

请把 NoChinaCDN 和 APIRules 放在最前面

使用中国区账号（App Store + iCloud）

AppleRules 直连

AppleCDNRules 直连

AppleNoChinaCDNRules 代理

AppleAPIRules 直连

使用美国区账号（App Store + iCloud）

AppleRules 直连

AppleCDNRules 直连

AppleNoChinaCDNRules 代理

AppleAPIRules 代理

建议 AppleAPIRules 依然直连，上文是根据上述文章给出的建议，请结合自身情况使用
