from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get("https://www.baidu.com")
# driver.get("https://www.douban.com")
# 在新的页面打开豆瓣
driver.execute_script("window.open('https://www.douban.com/')")
# print(driver.current_url) # driver.current_url获取当前的url
# 打印句柄
print(driver.window_handles)
# 切换到具体的第几个句柄（窗口）
driver.switch_to_window(driver.window_handles[1])
# 打印当前driver对应的url
print(driver.current_url)

"""
虽然在窗口中切换到了新的页面，但是在driver中并没有切换
如果想要在代码中做切换到新的页面，并且做一些爬虫，那么应该用driver.switch_to_window来切换到指定窗口，从driver.window_handlers中取出具体的第几个窗口
driver.window_handlers是一个列表，里面装的是窗口句柄
"""