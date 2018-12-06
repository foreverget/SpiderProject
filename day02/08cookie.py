from urllib import request
# 自己操作时，记得切换Ｃookie,因为cookie有生命周期
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36',
    'Cookie': 'anonymid=jo3nyq0jxow734; _r01_=1; depovince=GW; jebecookies=bd5f9c7c-054b-4f8e-8d2d-41d94019f946|||||; ick_login=741c3047-99a9-4f64-9cf6-07664fe2851e; _de=EA5778F44555C091303554EBBEB4676C696BF75400CE19CC; p=ba6cea0d5bdfe78011b3f7a36d7842b81; first_login_flag=1; ln_uact=970138074@qq.com; ln_hurl=http://hdn.xnimg.cn/photos/hdn121/20170428/1700/main_nhiB_aebd0000854a1986.jpg; t=304bccf1c5a34526a492f879b554af431; societyguester=304bccf1c5a34526a492f879b554af431; id=443362311; xnsid=7db50214; loginfrom=syshome; ch_id=10016; JSESSIONID=abc_8TvUx8c8y8o1VscEw; jebe_key=d24d069c-cdba-463d-a448-4d9742001e9e%7Ca022c303305d1b2ab6b5089643e4b5de%7C1544079214672%7C1%7C1544079214864; wp_fold=0',
}
#　爬取大鹏的主页
url = 'http://www.renren.com/880151247/profile'
req = request.Request(url,headers=headers)
resp = request.urlopen(req)
with open('renren.html','w') as fp:
    fp.write(resp.read().decode('utf-8'))