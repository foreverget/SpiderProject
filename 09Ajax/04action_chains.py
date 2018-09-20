"""
有时候需要在页面中进行的操作很多，那么可以使用鼠标行为链类Action来完成。比如，最简单的要将鼠标移动到某个元素上执行点击事件
"""
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
driver = webdriver.Chrome()
driver.get("https://www.baidu.com")

inputTag = driver.find_element_by_id("kw")
submitTag = driver.find_element_by_id("su")

actions = ActionChains(driver)
actions.move_to_element(inputTag)
actions.send_keys_to_element(inputTag,'python')
actions.move_to_element(submitTag)
actions.click(submitTag)
actions.perform()
"""
其他的一些行为链：
click_and_hold(element)：点击但不松开鼠标
context_click(element)：右键点击
double_click(element)：双击
更多行为链详情请参考：https://selenium-python.readthedocs.io/api.html
"""