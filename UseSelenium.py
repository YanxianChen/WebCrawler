# 使用selenium模拟浏览器进行抓取, 需先下载浏览器驱动geckodriver或者chromedriver
# 本机存放在"/usr/bin/"目录下,且已经在环境变量中设置好了
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import time

#要访问的网页
url = 'http://www.santostang.com/2017/03/02/hello-world/'

#浏览器程序的所在路径
binary = FirefoxBinary(r'/usr/bin/firefox')

driver = webdriver.Firefox(firefox_binary=binary)
driver.get(url)
driver.switch_to.frame(driver.find_element_by_css_selector("iframe[title='livere']"))

# load_more = driver.find_element_by_css_selector('button.more-btn')
# print(load_more.text)

i = 1   #评论序号
try:
    load_more = driver.find_element_by_css_selector('button.more-btn')
    for page in range(0,10):
        print(page)
        load_more.click()
        time.sleep(2)
except:
    print('评论已全部加载')

comments = driver.find_elements_by_css_selector('div.reply-content')
for each_comment in comments:
    content = each_comment.find_element_by_tag_name('p')
    print(str(i)+'. '+content.text)
    i += 1