from urllib import parse
"""
用浏览器发送请求的时候，如果url中包含了中文或者其他特殊字符，那么浏览器会自动的给我们进行编码。
而如果使用代码发送请求，那么就必须手动的进行编码，这时候就应该使用urlencode函数来实现。
urlencode可以把字典数据转换为URL编码的数据。
"""
data = {'name':'爬虫基础','greet':'hello world','age':100}
qs = parse.urlencode(data)
print(qs)

print("----------------------------解码----------------------------")
from urllib import parse
"""
parse_qs可以将经过编码后的url参数进行解码。
"""
qs = "name=%E7%88%AC%E8%99%AB%E5%9F%BA%E7%A1%80&greet=hello+world&age=100"
print(parse.parse_qs(qs))