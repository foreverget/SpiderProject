from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get("https://www.baidu.com")
print(driver.page_source)
time.sleep(3)
driver.close() # 关闭当前页面
driver.quit() # 退出整个浏览器