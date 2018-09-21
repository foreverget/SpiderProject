from lxml import etree

def parse_text():
    # 案例1：直接利用etree将字符串解析为HTML文档
    """
    lxml会自动修改ＨＴＭＬ代码，补全body、html标签
    """
    text = """
    <table class="tablelist" cellpadding="0" cellspacing="0">
                    <tbody><tr class="h">
                        <td class="l" width="374">职位名称</td>
                        <td>职位类别</td>
                        <td>人数</td>
                        <td>地点</td>
                        <td>发布时间</td>
                    </tr>
                                    <tr class="even">
                        <td class="l square"><a target="_blank" href="position_detail.php?id=44414&amp;keywords=&amp;tid=0&amp;lid=2218">24491-IP 商务合作负责人（深圳）</a></td>
                        <td>产品/项目类</td>
                        <td>1</td>
                        <td>深圳</td>
                        <td>2018-09-21</td>
                    </tr>
                                    <tr class="odd">
                        <td class="l square"><a target="_blank" href="position_detail.php?id=44409&amp;keywords=&amp;tid=0&amp;lid=2218">SNG03-互动视频web前端开发（专场）（深圳）</a></td>
                        <td>技术类</td>
                        <td>5</td>
                        <td>深圳</td>
                        <td>2018-09-21</td>
                    </tr>
                                    <tr class="even">
                        <td class="l square"><a target="_blank" href="position_detail.php?id=44401&amp;keywords=&amp;tid=0&amp;lid=2218">28096-腾讯音乐商业化广告产品经理（深圳）</a></td>
                        <td>产品/项目类</td>
                        <td>1</td>
                        <td>深圳</td>
                        <td>2018-09-21</td>
                    </tr>
                                    <tr class="odd">
                        <td class="l square"><a target="_blank" href="position_detail.php?id=44402&amp;keywords=&amp;tid=0&amp;lid=2218">28096-腾讯音乐商业营销策划经理（深圳）</a></td>
                        <td>市场类</td>
                        <td>1</td>
                        <td>深圳</td>
                        <td>2018-09-21</td>
                    </tr>
                                    <tr class="even">
                        <td class="l square"><a target="_blank" href="position_detail.php?id=44404&amp;keywords=&amp;tid=0&amp;lid=2218">28603-113 微信支付核心支付开发工程师(深圳)</a></td>
                        <td>技术类</td>
                        <td>1</td>
                        <td>深圳</td>
                        <td>2018-09-21</td>
                    </tr>
                                    <tr class="odd">
                        <td class="l square"><a target="_blank" href="position_detail.php?id=44405&amp;keywords=&amp;tid=0&amp;lid=2218">SNG17-社交产品总监</a><span class="hot">&nbsp;</span></td>
                        <td>产品/项目类</td>
                        <td>1</td>
                        <td>深圳</td>
                        <td>2018-09-21</td>
                    </tr>
                                    <tr class="even">
                        <td class="l square"><a target="_blank" href="position_detail.php?id=44406&amp;keywords=&amp;tid=0&amp;lid=2218">21557-前馈计算优化工程师</a></td>
                        <td>技术类</td>
                        <td>1</td>
                        <td>深圳</td>
                        <td>2018-09-21</td>
                    </tr>
                                    <tr class="odd">
                        <td class="l square"><a target="_blank" href="position_detail.php?id=44407&amp;keywords=&amp;tid=0&amp;lid=2218">21557-Android研发工程师(深圳）</a></td>
                        <td>技术类</td>
                        <td>2</td>
                        <td>深圳</td>
                        <td>2018-09-21</td>
                    </tr>
                                    <tr class="even">
                        <td class="l square"><a target="_blank" href="position_detail.php?id=44395&amp;keywords=&amp;tid=0&amp;lid=2218">28604-211 微信支付中小商户基础产品经理（深圳/广州）</a></td>
                        <td>产品/项目类</td>
                        <td>1</td>
                        <td>深圳</td>
                        <td>2018-09-21</td>
                    </tr>
                                    <tr class="odd">
                        <td class="l square"><a target="_blank" href="position_detail.php?id=44398&amp;keywords=&amp;tid=0&amp;lid=2218">MIG07-推荐系统架构师</a></td>
                        <td>技术类</td>
                        <td>1</td>
                        <td>深圳</td>
                        <td>2018-09-21</td>
                    </tr>
                                    <tr class="f">
                        <td colspan="5">
                            <div class="left">共<span class="lightblue total">2133</span>个职位</div>
                            <div class="right"><div class="pagenav"><a href="javascript:;" class="noactive" id="prev">上一页</a><a class="active" href="javascript:;">1</a><a href="position.php?lid=2218&amp;start=10#a">2</a><a href="position.php?lid=2218&amp;start=20#a">3</a><a href="position.php?lid=2218&amp;start=30#a">4</a><a href="position.php?lid=2218&amp;start=40#a">5</a><a href="position.php?lid=2218&amp;start=50#a">6</a><a href="position.php?lid=2218&amp;start=60#a">7</a><a href="position.php?lid=2218&amp;start=70#a">...</a><a href="position.php?lid=2218&amp;start=2130#a">214</a><a href="position.php?lid=2218&amp;start=10#a" id="next">下一页</a><div class="clr"></div></div></div>
                            <div class="clr"></div>
                        </td>
                    </tr>
                </tbody></table>
    """
    htmlElement = etree.HTML(text)
    # etree.HTML()出来的是一个Element类
    print(htmlElement)
    # etree.tostring()是按字符串序列化html文件
    print(etree.tostring(htmlElement))
    # 编解码后得到正常网页内容
    print(etree.tostring(htmlElement,encoding='utf-8').decode('utf-8'))

def parse_file():
    # 案例2： 从文档中读取内容进行解析
    parser = etree.HTMLParser(encoding='utf-8')
    htmlElement = etree.parse("tencent.html",parser=parser)
    print(etree.tostring(htmlElement, encoding='utf-8').decode('utf-8'))

if __name__ == '__main__':
    parse_file()
    # parse_text()

"""
笔记:
解析html字符串：使用lxml.etree.HTML进行解析，示例代码如下：
htmlElement = etree.HTML(text)
print(etree.tostring(htmlElement,encoding='utf-8').decode('utf-8'))

解析html文件：使用lxml.etree.parse进行解析。这个函数默认使用的是ＸＭＬ解析器。所以，如果碰到不规范的HTML代码解析会报错，
这个时候就需要创建自己创建'HTML'解析器，示例代码如下：
parser = etree.HTMLParser(encoding='utf-8')
htmlElement = etree.parse("tencent.html",parser=parser)

print(etree.tostring(htmlElement, encoding='utf-8').decode('utf-8'))

"""