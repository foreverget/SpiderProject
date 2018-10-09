import requests

from bs4 import BeautifulSoup

from selenium import webdriver

import os


def headers(referer):
    headers = {

        'Host': 'www.gugumh.com',

        'Accept-Encoding': 'gzip, deflate',

        'Accept-': 'zh-CN,zh;q=0.9',

        'Cache-Control': 'no-cache',

        'Connection': 'keep-alive',

        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.15 Safari/537.36',

        'Referer': '{}'.format(referer)

    }

    return headers


def Each_chapter():
    url = 'http://www.gugumh.com/manhua/200/'

    response = requests.get(url, headers(url))

    response.encoding = 'utf-8'

    sel = BeautifulSoup(response.text, 'lxml')

    total_html = sel.find('div', id='play_0')

    total_chapter = []

    for i in total_html.find_all('li'):
        total_title = i.get_text()  # 找到每一章的名字

        href = i.a['href']

        total_chapter.append(href)

        # 创造存放图片的文件夹

        dirName = u"{}".format(total_title)

        os.mkdir(dirName)

    return total_chapter


def Each_page(url):
    every_page_url = 'http://www.gugumh.com{}'.format(url)

    html = main(every_page_url)

    # print(browers.page_source)

    # 页数放在js中，只能使用selenium

    soups = BeautifulSoup(html, 'lxml')

    soup = soups.find('span', id="selectpage2")

    pages = soup.find_all('option')

    every_page = []

    for page in pages:
        every_page.append(page.get_text())

    return len(every_page)

    # browers.close()


def main(whole_url):
    chrome_options = webdriver.ChromeOptions()

    chrome_options.add_argument('--headless')

    browers = webdriver.Chrome(chrome_options=chrome_options)

    # 上面三行代码表示可以无界面爬取

    browers.get(whole_url)

    html = browers.page_source

    return html


if __name__ == '__main__':

    for i in Each_chapter():

        # print(i)

        each_page = Each_page(i)

        for a in range(1, each_page + 1):
            page = a

            whole_url = 'http://www.gugumh.com' + i + '?page=' + str(a)

            print(whole_url)
