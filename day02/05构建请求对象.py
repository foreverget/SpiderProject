
import urllib
url = "http://www.baidu.com"
headers = {
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
}
data = None
request = urllib.request.Request(url=url,headers=headers,data=data)
response = urllib.request.urlopen(request)