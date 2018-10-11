# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
"""
存储为json文件
"""
class QsbkPipeline(object):
    def __init__(self):
        self.fp = open("duanzi01.json","w",encoding='utf-8')

    def open_spider(self,spider):
        print("这是爬虫开始了")

    def process_item(self, item, spider):
        # item_json = json.dumps(item,ensure_ascii=False)
        item_json = json.dumps(dict(item), ensure_ascii=False)
        self.fp.write(item_json+'\n')
        return item

    def close_spider(self,spider):
        self.fp.close()
        print("这是爬虫结束了")
"""
优化存储方式1
"""
from scrapy.exporters import JsonItemExporter
class QsbkPipeline(object):
    def __init__(self):
        self.fp = open("duanzi02.json","wb")
        self.exporter = JsonItemExporter(self.fp,ensure_ascii=False,encoding='utf-8')
        self.exporter.start_exporting()


    def open_spider(self,spider):
        print("这是爬虫开始了")

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item

    def close_spider(self,spider):
        self.exporter.finish_exporting()
        self.fp.close()
        print("这是爬虫结束了")


"""
优化存储方式2
"""
from scrapy.exporters import JsonItemExporter,JsonLinesItemExporter
class QsbkPipeline(object):
    def __init__(self):
        self.fp = open("duanzi03.json","wb")
        self.exporter = JsonLinesItemExporter(self.fp,ensure_ascii=False,encoding='utf-8')
        self.exporter.start_exporting()


    def open_spider(self,spider):
        print("这是爬虫开始了")

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item

    def close_spider(self,spider):
        # self.exporter.finish_exporting()
        self.fp.close()
        print("这是爬虫结束了")

"""
JsonItemExporter和JsonLinesItemExporter
保存为json的时候可以使用这两个类，让操作更简单．
前者是每次把数据添加到内存中，最后统一写到磁盘中．好处是，存储的数据是一个满足json规则的数据,
坏处是磁盘占用量大，比较耗内存
后者每次调用export_item的时候就把这个item存储到磁盘中．坏处是每一个字典是一行，整个文件不满足json格式文件．
好处是每次处理数据的时候就直接存储到了磁盘中，这样不会耗内存，数据也比较安全．

"""