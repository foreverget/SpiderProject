import urllib.request
import time
from lxml import etree


def handle_url(page,base_url):

    url = base_url + str(page) + '/'

    headers = {
        'User - Agent': 'Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 65.0.3325.181Safari / 537.36'
    }

    req = urllib.request.Request(url=url,headers=headers)
    res = urllib.request.urlopen(req)
    return res.read().decode('utf-8')
    # with open('test58.html','w',encoding='utf-8') as fp:
    #     fp.write(res.read().decode('utf-8'))

def search_rentinginfo(html):
    html_stree = etree.HTML(html)
    url_list = html_stree.xpath('/html/body/div/div/div/div/ul/li/div/h2/a/@href')
    # print(url_list)
    return url_list

def download_page():
    pass

def main():

    base_url = 'http://sz.58.com/chuzu/pn'

    start_page = int(input('输入开始页：'))
    end_page = int((input('输入结束页：')))


    for page in range(start_page,end_page+1):

        html = handle_url(page,base_url)
        time.sleep(5)
        # print(html)
        info_list = search_rentinginfo(html)

        start = 0
        for info in info_list:

            if start >= 5:
                break
            # print(info)

            new_info = urllib.request.urlopen(info)
            time.sleep(5)
            # print(new_info.read().decode('utf-8'))
            newinfo_etree = etree.HTML(new_info.read().decode('utf-8'))

            payfor = newinfo_etree.xpath('normalize-space(/html/body/div/div/div/div/div/div/span/b/text())')
            payfor_type = newinfo_etree.xpath('normalize-space(/html/body/div/div/div/div/div/div/span[2]/text())')
            rent_type = newinfo_etree.xpath('normalize-space(/html/body/div/div/div/div/div/ul/li[1]/span[2]/text())')
            room_type = newinfo_etree.xpath('normalize-space(/html/body/div/div/div/div/div/ul/li[2]/span[2]/text())')
            floor = newinfo_etree.xpath('normalize-space(/html/body/div/div/div/div/div/ul/li[3]/span[2]/text())')
            place = newinfo_etree.xpath('normalize-space(/html/body/div/div/div/div/div/ul/li[4]/span[2]/a/text())')
            area = newinfo_etree.xpath('normalize-space(/html/body/div/div/div/div/div/ul/li[5]/span[2]/a/text())')
            street = newinfo_etree.xpath('normalize-space(/html/body/div/div/div/div/div/ul/li[6]/span[2]/text())')
            phone = newinfo_etree.xpath('normalize-space(/html/body/div/div/div/div/div/span/text())')

            print(payfor,payfor_type,rent_type,room_type,floor,place,area,street,phone)
            start += 1

if __name__ == '__main__':
    main()









