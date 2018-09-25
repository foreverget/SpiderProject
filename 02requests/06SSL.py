import requests
"""
对于那些已经被信任的SSL整数的网站，比如https://www.baidu.com/，那么使用requests直接就可以正常的返回响应。
"""
resp = requests.get('http://www.12306.cn/mormhweb/',verify=False)
print(resp.content.decode('utf-8'))