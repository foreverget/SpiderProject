from selenium import webdriver
import json
from time import sleep
driver = webdriver.Chrome()

driver.get('https://www.douyu.com/directory/all')

driver.implicitly_wait(10)

fp = open('./douyu.txt', 'w', encoding='utf-8')

# 循环爬取每一页的数据
while True:
    sleep(3)
    # 获取页面所有的li
    li_list = driver.find_elements_by_xpath('//ul[@id="live-list-contentbox"]/li')
    # print(li_list)
    #对每一个li进行处理
    items = []
    for li in li_list:
        title = li.find_element_by_xpath('.//h3').text.strip('\n')
        category = li.find_element_by_xpath('.//span[@class="tag ellipsis"]').text
        name = li.find_element_by_xpath('.//span[@class="dy-name ellipsis fl"]').text
        hot = li.find_element_by_xpath('.//span[@class="dy-num fr"]').text
        item = {
            'title': title,
            'category': category,
            'name': name,
            'hot': hot
        }
        items.append(item)
    fp.write(json.dumps(items, ensure_ascii=False))
    # 爬完了，进入下一页
    #
    driver.execute_script('document.documentElement.scrollTop=10000')
    # 东西没加载完
    sleep(3)
    # 判断下一页能否点
    if driver.page_source.find('shark-pager-disable-next') != -1:
        # 下一页无法点击， 表示是最后一页
        # 退出循环
        break
    # 不是下一页，则点击下一页
    driver.find_element_by_xpath('//a[@class="shark-pager-next"]').click()
# 关闭文件
fp.close()
# 关闭浏览器
driver.quit()
