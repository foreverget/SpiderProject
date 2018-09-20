from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get("https://www.baidu.com")
# 获取当前网页下所有cookie信息
for cookie in driver.get_cookies():
    print(cookie)

print("="*30)
print(driver.get_cookie("PSTM"))  # 获取某个cookie
driver.delete_cookie("PSTM")  # 删除某个cookie
# driver.delete_all_cookies() # 删除所有cookies

print("="*30)
print(driver.get_cookie("PSTM"))