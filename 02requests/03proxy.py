import requests

url = "http://httpbin.org/get"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36',
}

proxy = {
    'https':'61.135.217.7:80'
}

resp = requests.get(url,headers=headers,proxies=proxy)
with open('xx.html','w',encoding='utf-8') as fp:
    fp.write(resp.text)


# 练习2
import requests

url = 'http://www.baidu.com/s'

data = {
    'wd': 'ip'
}

proxies = {
    'http': '115.153.173.238:61234'
}

r = requests.get(url=url, params=data, proxies=proxies)
r.encoding = 'utf-8'

with open('./baiduip.html', 'w', encoding='utf-8') as fp:
    fp.write(r.text)