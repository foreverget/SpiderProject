from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
import time
driver = webdriver.Chrome()
driver.get("https://www.baidu.com")
submitBtn = driver.find_element_by_id("su")
print(type(submitBtn))
print(submitBtn.get_attribute("value"))
driver.save_screenshot("baidu.png")