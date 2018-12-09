import requests
resp = requests.get('https://www.baidu.com/')
print(resp.cookies)
print(resp.cookies.get_dict())