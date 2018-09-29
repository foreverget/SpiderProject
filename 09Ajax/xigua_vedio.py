from selenium import webdriver
from time import sleep
from urllib.request import urlretrieve
import string
import random

options = webdriver.ChromeOptions()
options.add_argument('headless')

driver = webdriver.Chrome(chrome_options=options)

driver.get('https://www.ixigua.com/')

sleep(2)

# 获取视频详情页的连接
a_list = driver.find_elements_by_xpath('//a[@class="link"]')

# 获取a标签中href地址。
href_list = [a.get_attribute('href') for a in a_list]


# 随机文件名
def random_str(size=64):
    base_str = string.ascii_letters + string.digits
    return ''.join(random.choice(base_str) for _ in range(size))

# print(href_list)
# 循环访问详情页地址
for href, i in zip(href_list, range(len(href_list))):
    driver.get(href)
    sleep(2)
    # 找到页面中要下载的视频地址。
    src = driver.find_element_by_xpath('//div[@class="player-wrap"]//video').get_attribute('src')
    # print(src)
    # 下载视频
    urlretrieve(src, './xigua/' + random_str() + '.mp4')
    print('第%d个视频下载完成' % (i+1,))

driver.quit()