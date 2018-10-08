import os
import urllib.request
import urllib.parse


url = 'http://fanyi.baidu.com/sug'

word = input('请输入您要查找的英文单词：')
# 构造post请求的data。
data = {
    'kw': word,
}
# 编码
data = urllib.parse.urlencode(data).encode('utf-8')

response = urllib.request.urlopen(url=url, data=data)

# print(response.read().decode('utf-8'))
# json_string = response.read().decode('utf-8')
# import json
# json_obj = json.loads(json_string)
# json_string = json.dumps(json_obj,ensure_ascii=False)
#

# with open('./json','w',encoding='utf-8') as fb:
#     fb.write(json_string)
# with open('ret.json', 'wb') as file:
#     file.write(response.read())

json_string = response.read().decode('utf-8')
import json
# 将json字符串转换为json对象
json_obj = json.loads(json_string)
# 将json对象变成普通字符串，并且禁止使用默认的ascii编码方式
json_string = json.dumps(json_obj, ensure_ascii=False)

# print(response.read().decode('utf-8'))
# 二进制模式下无法修改编码方式，所以把b去掉
with open('ret.json', 'w', encoding='utf-8') as file:
    file.write(json_string)