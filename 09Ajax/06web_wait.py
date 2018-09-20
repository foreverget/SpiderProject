from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
driver.get("https://www.douban.com")
# driver.implicitly_wait(10) # 隐式等待

# 显式等待
element = WebDriverWait(driver,10).until(
    EC.presence_of_all_elements_located((By.ID,'form_email'))
)
print(element)