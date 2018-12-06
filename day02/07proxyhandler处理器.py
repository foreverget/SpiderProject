from urllib import request
# 不使用代理
url = 'http://httpbin.org/ip'
resp1 = request.urlopen(url)
print(resp1.read())

# 使用代理
handler = request.ProxyHandler({"http":"221.210.120.153:54402"}) #使用ProxyHandler，传入代理创建一个hadler
opener = request.build_opener(handler)# 使用上面创建的handler构建一个opener
resp2 = opener.open(url)
print(resp2.read())