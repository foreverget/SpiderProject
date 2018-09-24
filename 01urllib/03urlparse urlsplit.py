from urllib import request,parse
"""
有时候拿到一个url，想要对这个url中的各个组成部分进行分割，那么这时候就可以使用urlparse或者是urlsplit来进行分割。
"""

url = 'http://www.baidu.com/s?username=zhiliao'

result = parse.urlsplit(url)
# result = parse.urlparse(url)

print('scheme:',result.scheme)
print('netloc:',result.netloc)
print('path:',result.path)
print('query:',result.query)