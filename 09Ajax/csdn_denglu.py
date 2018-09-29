from selenium import webdriver
from time import sleep
"""
模拟登陆CSDN
"""
# 使用chrome headless 代替phantomJS

options = webdriver.ChromeOptions()
options.add_argument('headless')

driver = webdriver.Chrome(chrome_options=options)

driver.get('https://passport.csdn.net/account/login')


driver.implicitly_wait(10)

driver.find_element_by_link_text('账号登录').click()

driver.find_element_by_id('username').send_keys('13580416180')

driver.find_element_by_id('password').send_keys('jiangwei112')


driver.find_element_by_xpath('//input[@class="logging"]').click()

driver.save_screenshot('csdn.png')

driver.quit()

