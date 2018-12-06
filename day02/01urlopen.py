

from urllib import request

resp = request.urlopen("http://www.baidu.com")
print(resp.getcode()) # 获取状态码
print(resp.geturl()) # 获取url
print(resp.getheaders()) # 获取请求头
print(resp)#　查看urlopen返回值类型
print(resp.read())# 查看所有内容
print(resp.read().decode("utf-8")) # 将字节类型转化为字符串类型
print(resp.readline()) # 查看第一行内容
print(resp.readlines())#　查看所有内容，并返回在一个列表中
