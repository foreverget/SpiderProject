
import requests
from bs4 import BeautifulSoup

url = "https://hr.tencent.com/position.php?keywords=python&lid=0&tid=0"
headers = {
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',
    }

response = requests.get(url,headers=headers)
soup = BeautifulSoup(response.text,'lxml')

# print(soup.prettify()) # 查看获取的解析后网页

# # １.获取所有的tr标签
# trs = soup.find_all('tr')
# for tr in trs:
#     print(tr)
#     print(type(tr))

# # 2.获取第二个tr标签
# tr2 = soup.find_all('tr',limit=2)[1]
# print(tr2)

# # 3.获取所有class等于even的标签
# # trs = soup.find_all('tr',class_ = 'even')
# trs = soup.find_all('tr',attrs={'class':'even'})
# for tr in trs:
#     print(tr)

# # 4.获取所有id等于test,class等于test的a标签
# # trs = soup.find_all('a',id='test',class_='test')
# trs = soup.find_all('a',attrs={"id":'test','class':'test'})
# for tr in trs:
#     print(tr)

# 5.获取所有a标签的href属性
aList = soup.find_all('a')
for a in aList:
    # 1.通过小标的方式
    href = a['href']
    print(href)
#     # 2.通过attr属性的方式
#     href = a.attrs['href']
#     print(href)

# 6.获取所有的职位信息(纯文本)
# trs = soup.find_all('tr')[1:-2]
# positions = []
# for tr in trs:
#     tds = tr.find_all('td')
#     title = tds[0].string
#     category = tds[1].string
#     nums = tds[2].string
#     city = tds[3].string
#     pubtime = tds[4].string
#     position={
#         'title':title,
#         'category':category,
#         'nums':nums,
#         'city':city,
#         'pubtime':pubtime,
#     }
#     positions.append(position)
# print(positions)
# strings不能去除空格，stripped_strings能够去除空格
# trs = soup.find_all('tr')[1:-2]
# for tr in trs:
#     infos = list(tr.stripped_strings)
#     print(infos)