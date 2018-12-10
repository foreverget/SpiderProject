
import requests
from lxml import etree
import time
import pymysql
import re


conn = pymysql.connect(host='localhost',user='root',passwd='huang921118',db='doubanmovie',
                       port=3306,charset='utf8')
cursor = conn.cursor()

headers = {
    "User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36",
    "Host": "movie.douban.com",
}

def get_movie_url():
    response = requests.get(url,headers=headers)
    selector = etree.HTML(response.text)
    movie_hrefs = selector.xpath("//div[@class='hd']//a/@href")
    for movie_href in movie_hrefs:
        get_movie_info(movie_href)

def get_movie_info(url):
    movie = []
    response = requests.get(url,headers=headers)
    selector = etree.HTML(response.text)

    title = selector.xpath("//span[contains(@property,'itemreviewed')]/text()")
    director = selector.xpath("//div[@id='info']//span[1]//span[@class='attrs']/a/text()")
    main_actor = selector.xpath("//a[contains(@rel,'starring')]/text()")
    style = re.findall('<span property="v:genre">(.*?)</span>',response.text,re.S)
    country = re.findall('<span class="pl">制片国家/地区:</span>(.*?)<br/>',response.text,re.S)
    language = re.findall('<span class="pl">语言:</span>(.*?)<br/>',response.text,re.S)
    release_time = selector.xpath("//span[contains(@property,'initialReleaseDate')]/text()")
    time = selector.xpath("//span[contains(@property,'runtime')]/text()")
    score = selector.xpath("//strong[contains(@class,'rating_num')]/text()")


    # movie_detail = {
    #     'title':title,
    #     'director':director,
    #     'actors':main_actor,
    #     'style':style,
    #     'country':country,
    #     'language':language,
    #     'release_time':release_time,
    #     'time':time,
    #     'score':score,
    # }
    # movie.append(movie_detail)
    # print(movie)
    cursor.execute("insert into doubanmovie (title,director,main_actor,style,country,language,release_time,time,score) values (%s,%s,%s,%s,%s,%s,%s,%s,%s)",(str(title),str(director),str(main_actor),str(style),str(country),str(language),str(release_time),str(time),str(score)))



if __name__ == "__main__":
    urls = ["https://movie.douban.com/top250?start={}&filter=".format(str(i)) for i in range(0,250,25)]
    for url in urls:
        get_movie_url()
        time.sleep(2)
    conn.commit()