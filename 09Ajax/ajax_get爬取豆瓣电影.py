import urllib.request
import urllib.parse
import ssl

# 解决ssl证书问题
ssl._create_default_https_context = ssl._create_unverified_context


url = 'https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&'

# 输入页码
page = int(input('请输入您想获取的页码：'))
# start=0&limit=20
data = {
    'start': (page-1) * 20,
    'limit': 20,
}

data = urllib.parse.urlencode(data)

# url 拼接
url = url + data

# 创建request对象
request = urllib.request.Request(url=url)
response = urllib.request.urlopen(request)

print(response.read().decode('utf-8'))

