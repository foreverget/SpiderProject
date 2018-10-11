# -*- coding: utf-8 -*-
import scrapy
from ..items import QsbkItem

class QsbkSpiderSpider(scrapy.Spider):
    name = 'qsbk_spider'
    allowed_domains = ['qiushibaike.com']
    start_urls = ['https://www.qiushibaike.com/text/page/1/']

    def parse(self, response):
        duanzidivs = response.xpath("//div[@id='content-left']/div")
        # items = [] # 不使用yield
        for duanzidiv in duanzidivs:
            author = duanzidiv.xpath(".//h2/text()").get().strip()
            content = duanzidiv.xpath(".//div[@class='content']//text()").getall()
            content = "".join(content).strip()
            item = QsbkItem(author=author,content=content)
            # duanzi = {"author":author,"content":content}
            # yield duanzi
            # items.append(item) # 不使用yield
            # return items # 不使用yield
            yield item
"""
笔记:
１、response是一个scrapy.http.response.html.HttpResponse对象．可以执行xpath和css语法提取数据
２、提取出来的数据，是一个Selector或者SelectorList对象．如果想要获取其中的字符串，那么应该执行getall()或者get（）方法
3、getall()方法：获取的Ｓelector中所有的文本，返回的是一个列表
４、get()方法：获取的是Selector()的第一个文本，返回的是一个列表
５、如果数据解析回来，要传给pipeline处理，那么可以使用yield来返回数据.或者收集所有的数据，最后统一return返回
６、item：建议在iteｍ中定义好模型，以后不要使用字典
７、pipeline：这个专门用来保存数据的．其中，有三个方法经常使用：
    .open_spider(self,spider):当爬虫打开的时候执行
    .process_spider(self,spider):当爬虫有item传过来的时候会被调用
    .close_spider(self,spider):当爬虫关闭的时候会被调用
要激活pipeline,应该在settings.py中设置TIME_PIPELINES
"""

