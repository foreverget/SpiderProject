from urllib import request
from http.cookiejar import MozillaCookieJar

cookiejar = MozillaCookieJar("cookie.txt")
handler = request.HTTPCookieProcessor(cookiejar)
opener = request.build_opener(handler)

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'
}
req = request.Request('http://httpbin.org/cookies/set?course="spider"',headers=headers)

resp = opener.open(req)
print(resp.read().decode("utf-8"))
cookiejar.save(ignore_discard=True,ignore_expires=True)