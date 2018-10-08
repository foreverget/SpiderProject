import requests
"""
requests通过get请求网页，响应、以及查看响应相关内容
"""
kw = {'wd':'中国'}

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}

# params 接收一个字典或者字符串的查询参数，字典类型自动转换为url编码，不需要urlencode()
response = requests.get("http://www.baidu.com/s", params = kw, headers = headers)

# 查看响应内容，response.text 返回的是Unicode格式的数据
print(response.text)

# 查看响应内容，response.content返回的字节流数据
print(response.content)

# 查看完整url地址
print(response.url)

# 查看响应头部字符编码
print(response.encoding)

# 查看响应码
print(response.status_code)


# 练习2
import requests


url = 'https://www.baidu.com'
#
# r = requests.get(url=url)
#
# # 查看内容
# print(r.text)
#
# # 查看编码
# print(r.encoding)
#
# # 转换编码
# r.encoding = 'utf-8'
#
# print(r.text)


# get请求带参数

r = requests.get(url=url)
r.encoding = 'utf-8'

# 查看请求地址
print(r.url)

print(r.content)
# 状态码
print(r.status_code)

# 头部信息
print(r.headers)
# print(r.text)
# with open('./baidu58.html', 'w', encoding='utf-8') as fp:
#     fp.write(r.text)