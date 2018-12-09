import requests

url = "http://httpbin.org/get"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36',
}

proxy = {
    'http': '221.210.120.153:54402'
}

resp = requests.get(url,headers=headers,proxies=proxy)
print()
with open('xx.html','w',encoding='utf-8') as fp:
    fp.write(resp.text)