# Rules

A uniform way to manage all the rules.

## Ad Blocking

Ad Blocking can be achieved via `REJECT` or similar methods in Loon/Surge. But 
as [Hackl0us](https://github.com/Hackl0us/SS-Rule-Snippet#%E5%85%B3%E4%BA%8E%E5%B9%BF%E5%91%8A%E5%B1%8F%E8%94%BD)
points out, rules for ad-blocking needs constantly updates and it can be hard to
maintain.

Another thing is that rules/domains for ad blocking often comes in the number of
thousands (over 20k easily) and it should be set in the first few rules/filters
in Loon/Surge/Qx. Haven't tested, but my guess is that it will definitely add
burden, which might be a issue in mobile devices.

Ended up with AdGuard on mac and still Ad Blocking rules in iOS.

## Rules/Filter priority

See [Loon 分流规则](https://github.com/dunlanl/FuGfConfig#loon-%E5%88%86%E6%B5%81%E8%A7%84%E5%88%99) 
and [推荐排序](https://github.com/sve1r/Rules-For-Quantumult-X#3%E6%8E%A8%E8%8D%90%E6%8E%92%E5%BA%8F)

Priority (High to low): !! Rules/Filter in Plugin still __OVERWRITE__ this !!

Not sure if China.list is needed since it all go FINAL(漏网之鱼)

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
* 如需细化流媒体如「Youtube.list」需要加在「ForeignMedia.list」之前。
* 如需应用类的如「Telegram.list、Google.list、PayPal.list」需要加在「Global.list」之前。

About Apple ID:

使用美国区账号（App Store + iCloud）
AppleRules 直连 AppleCDNRules 直连 AppleNoChinaCDNRules 代理 AppleAPIRules 代理

建议 AppleAPIRules 依然直连，上文是根据上述文章给出的建议，请结合自身情况使用

### AdGuard resources

[Chinese specify ad list for AdGuard](https://anti-ad.net/)

[A more functional blocklist (functionality over blocking)](https://oisd.nl/)

[AdGuard and Clash X Pro working together](https://www.v2ex.com/t/787455)

[AdGuard and Clash on Android](https://blog.ichr.me/post/adguard-with-clash/)


## iOS (Loon/Qx/Surge)

Haven't tried surge yet, but prefer Loon over Qx because of UI thought I do like 
the "link profile" feature in Qx, seems to work better than simply iCloud sync
in Loon

[Loon Plugin Priority](https://github.com/chiupam/tutorial/blob/master/Loon/Plus/Plugin_Summary.md): 
Plugin in essence is just a mini conf, but it's not recommended to put scripts
such as auto sign-in there as it's not possible to change `cron` settings。

[Rules/Filters]:
Aside from custom ones, all from [blackmatrix7](https://github.com/blackmatrix7/ios_rule_script/)

Custom ones should be put in front of all the other remote ones.


## macOS (Clash X Pro/Loon)

Loon can be installed and it runs fine with macs with Apple Silicon.

## Ref

[LoonExampleConfig](https://github.com/Loon0x00/LoonExampleConfig)

[Loon 不完全教程](https://www.notion.so/Loon-f0a98c39f5224c09b281c79837380431)

[Quantumult X 不完全教程](https://www.notion.so/Quantumult-X-1d32ddc6e61c4892ad2ec5ea47f00917)

[【小白教程】10分钟搞懂分流策略 | 分流规则、策略组详解，如何DIY自己的专属分流策略，新手避坑指南！]https://w37fhy.com/archives/776

[Rules-For-Quantumult-X](https://github.com/sve1r/Rules-For-Quantumult-X)

[关于策略组的理解](https://github.com/Fndroid/jsbox_script/wiki/%E5%85%B3%E4%BA%8E%E7%AD%96%E7%95%A5%E7%BB%84%E7%9A%84%E7%90%86%E8%A7%A3)

[ios_rule_script](https://github.com/blackmatrix7/ios_rule_scrip): Most detailed
filter and rewrite repo. I found, but it's not that personal and some general 
list contains 10k-20k entries