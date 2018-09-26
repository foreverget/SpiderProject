import urllib.request
import urllib.parse


url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname'

data = {
    'cname': '深圳',
    'pid': '',
    'pageIndex': '5',
    'pageSize': '10'
}

data = urllib.parse.urlencode(data).encode('utf-8')

# 创建请求对象
request = urllib.request.Request(url=url, data=data)

response = urllib.request.urlopen(request)

print(response.read().decode('utf-8'))