from urllib import request,parse
from http.cookiejar import CookieJar

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'
}

def get_opener():
    cookiejar = CookieJar() # 1.1 创建一个cookiejar对象
    handler = request.HTTPCookieProcessor(cookiejar) # 1.2 使用cookiejar对象创建一个HTTPCookieProcess对象
    opener = request.build_opener(handler) # 1.3 使用上一步创建的handler创建一个opener
    return opener

# 1.4 使用opener发送登陆的请求(人人网的邮箱和密码)
def login_renren(opener):
    data = {"email": "970138074@qq.com", "password": "pythonspider"}
    data = parse.urlencode(data).encode('utf-8')
    login_url = "http://www.renren.com/PLogin.do"
    req = request.Request(login_url, headers=headers, data=data)
    opener.open(req)

def visit_profile(opener):
    url = 'http://www.renren.com/880151247/profile'
    req = request.Request(url,headers=headers)
    resp = opener.open(req)
    with open('renren2.html','w') as fp:
        fp.write(resp.read().decode("utf-8"))

if __name__ == '__main__':
    """
    １.登录
    2.访问个人主页
    """
    opener = get_opener()
    login_renren(opener)
    visit_profile(opener)
