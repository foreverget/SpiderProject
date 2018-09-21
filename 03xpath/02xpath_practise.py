from lxml import etree
# 1.获取所有的tr标签
# 2.获取第2个tr标签
# 3.获取所有class等于even的标签
# 4.获取所有a标签的href属性
# 5.获取所有的职位信息
parser = etree.HTMLParser(encoding='utf-8')
html = etree.parse("tencent.html",parser=parser)
def get_tr():
    trs = html.xpath("//tr")
    for tr in trs:
        print(etree.tostring(tr,encoding='utf-8').decode("utf-8"))

def get_tr2():
    trs = html.xpath("//tr[2]")[0]
    print(etree.tostring(trs,encoding='utf-8').decode("utf-8"))

def get_class_even():
    trs = html.xpath("//tr[@class='even']")
    for tr in trs:
        print(etree.tostring(tr,encoding="utf-8").decode("utf-8"))

def get_href():
    """
    //a[@href]:获取所有拥有href属性的a标签
    //a/@href ：获取所有href属性的值
    """
    aList = html.xpath("//td[@class='l square']//a/@href")
    for a in aList:
        print("http://hr.tencent.com/" + a)

def get_position():
    positions = []
    trs = html.xpath("//tr[position()<12]")
    for tr in trs[1:]:
        # print(etree.tostring(tr,encoding="utf8").decode("utf8"))
        #在某个标签下，执行xpath函数，获取这个标签下的子孙元素，那么应该在//之前加个"."，代表是在当前元素下获取
        href = tr.xpath(".//a/@href")[0]
        fullurl = "http://hr.tencent.com/" + href
        # title = tr.xpath(".//a/text()")
        title = tr.xpath("./td[1]//text()")[0]
        category = tr.xpath("./td[2]/text()")[0]
        nums = tr.xpath("./td[3]/text()")[0]
        address = tr.xpath("./td[4]/text()")[0]
        pubtime = tr.xpath("./td[5]/text()")[0]
        position = {
            'url':fullurl,
            'title':title,
            'category':category,
            'nums':nums,
            'address':address,
            'pubtime':pubtime
        }
        positions.append(position)
    print(positions)


if __name__ == '__main__':
    # get_tr() # 1.获取所有的tr标签
    # get_tr2() # 获取第2个tr标签
    # get_class_even() # 获取所有class等于even的tr标签
    # get_href() #获取所有职位的href属性值
    get_position()

"""
xpath和lxml爬取内容学习笔记：
lxml结合xpath注意事项：
1、使用xpath语法，应该使用Element.xpath()方法，来执行xpath的选择，示例代码如下:
trs = html.xpath("//tr[position()<12]")
2、获取某个标签的属性，示例代码如下：
href = tr.xpath(".//a/@href")
3、获取文本，是通过xpath中的text()函数。示例代码如下：
title = tr.xpath(".//a/text()")
4、如果想要在某个标签下，再执行xpath函数，获取这个标签下的子孙元素，那么应该在斜杠之前加个"."，代表是在当前元素下获取
href = tr.xpath(".//a/@href") # 获取tr标签下的a标签的href属性值
address = tr.xpath("./td[4]/text()") # 获取tr标签下的第4个td标签的文本
"""
