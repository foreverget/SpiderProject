import json

import requests
from bs4 import BeautifulSoup


def handler_url(base_url, page):
    url = base_url % page
    return url


def main():
    base_url = 'http://sou.zhaopin.com/jobs/searchresult.ashx?jl=深圳&kw=python&sm=0&sg=492ea9f658fc4b148522d926e6717ce9&p=%d'
    start_page = int(input('请输入起始页:'))
    end_page = int(input('请输入结束页:'))
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.104 Safari/537.36'
    }

    for page in range(start_page, end_page +1):
        # 拼接url
        url = handler_url(base_url, page)
        # 发起http请求
        r = requests.get(url=url, headers=headers)
        # 创建bs4对象
        soup = BeautifulSoup(r.text, 'lxml')
        # 找出所有的tr
        table_list = soup.select('#newlist_list_content_table > table')[1:]
        # print(table_list)
        # 循环取出table中的职位名称工资等信息

        job_list = []
        for table in table_list:
            job = {}
            job['job_name'] = table.select('.zwmc')[0].select('a')[0].get_text()

            job['company_name'] = table.select('.gsmc')[0].select('a')[0].string
            job['salary'] = table.select('.zwyx')[0].string
            job['place'] = table.select('.gzdd')[0].string
            job_list.append(job)

        # 打印到文件中
        # json
        string = json.dumps(job_list, ensure_ascii=False)
        # 写入文件
        with open('zilian.json', 'w', encoding='utf-8') as fp:
            fp.write(string)



if __name__ == '__main__':
    main()