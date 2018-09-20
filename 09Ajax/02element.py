from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get("https://www.baidu.com")

# 通过id获取
inputTag = driver.find_element_by_id('kw')
inputTag.send_keys('python')

# 通过name获取
inputTag2 = driver.find_element_by_name('wd')
inputTag2.send_keys('java')

# 通过类名获取
inputTag3 = driver.find_element_by_class_name('s_ipt')
inputTag3.send_keys('ruby')

# 通过xpath获取
inputTag4 = driver.find_element_by_xpath('//input[@id="kw"]')
inputTag4.send_keys("go")

# 通过css选择器获取
inputTag5 = driver.find_element_by_css_selector(".quickdelete-wrap > input")
inputTag5.send_keys("C#")

"""
注意！
element是获取的满足条件的第1个元素,elements获取的是所有满足条件的元素，以列表形式返回
如果只是想要解析网页中的数据，那么建议将网页源代码扔给lxml来解析。因为lxml底层使用的是C语言，，解析起来效率更高
如果想要对元素进行一些操作，比如，给一个文本框输入值，或者点击某个按钮，那么就必须使用selenium给我们提供的查找元素的方法。
"""