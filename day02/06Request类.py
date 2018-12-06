

from urllib import request,parse

url = 'https://www.lagou.com/zhaopin/Python/?labelWords=label'
headers = {
    'Accept':'application/json, text/javascript, */*; q=0.01',
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) '
                 'Chrome/70.0.3538.110 Safari/537.36',
    'Referer':'https://www.lagou.com/zhaopin/Python/?labelWords=label',
}
data = {
    'first':'true',
    'pn':'1',
    'kd':'Python',
}

req = request.Request(url,headers=headers,data=parse.urlencode(data).encode('utf-8'),method='POST')
print(req)
resp = request.urlopen(req)
print(resp.read().decode('utf-8'))