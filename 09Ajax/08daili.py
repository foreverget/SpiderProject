from selenium import webdriver
options = webdriver.ChromeOptions()
options.add_argument("--proxy-server=http://60.191.201.38:45461")

driver = webdriver.Chrome(chrome_options=options)
driver.get("http://httpbin.org/ip")