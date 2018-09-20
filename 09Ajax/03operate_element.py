"""
操作表单元素：
常见的表单元素：input、button、checkbox、select
"""
from selenium import webdriver
import time
driver = webdriver.Chrome()


# 操作输入框，分两步：第1步找到这个元素，第2步使用send_keys(value),将数据填充进去。
driver.get("https://www.baidu.com")
# print(driver.page_source)
inputTag = driver.find_element_by_id('kw')
inputTag.send_keys('python')
time.sleep(3)
# 使用clear方法可以清除输入框中的内容。
inputTag.clear()

# 操作checkbox:要选中checkbox标签，网页中是通过鼠标点击的。因此，想要选中checkbox标签，那么先找到这个标签，再执行click事件
driver.get('https://www.douban.com')
rememberBtn = driver.find_element_by_name('remember')
rememberBtn.click()
# rememberBtn.click() # 执行两次则代表取消选中

# 操作select select元素不能直接点击。因为点击后还需要选中元素，这时候selenium就专门为select标签提供了一个selenium.webdriver.support.ui.Select.
# 将获取的元素当成参数传到这个类中，创建这个对象。以后就可以使用这个对象进行选择了
# from selenium.webdriver.support.ui import Select
# driver.get('http://www.dobai.cn/')
# selectBtn = Select(driver.find_element_by_name('jumpMenu'))
# selectBtn.select_by_index(1) # 通过索引
# selectBtn.select_by_value('https://m.95xiu.com/') # 通过value值
# selectBtn.select_by_visible_text('95秀客户端') # 通过可见文本
# selectBtn.deselect_all() #取消所有的选中

# 操作按钮 操作按钮有很多种方式，比如单击、右击、双击。这里以最常用的单击为例进行演示
from selenium.webdriver.support.ui import Select
driver.get("https://www.baidu.com")
inputTag2 = driver.find_element_by_id("kw")
inputTag2.send_keys("重庆大学")
submitTag = driver.find_element_by_id("su")
submitTag.click()