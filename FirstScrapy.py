#!/user/bin/python
# coding: UTF-8
import requests
from bs4 import BeautifulSoup

#获取网页
link = "http://www.santostang.com/"
headers = {
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
    }
r = requests.get(link, headers= headers)

#解析网页
soup = BeautifulSoup(r.text, "lxml")
title = soup.find("h1", class_="post-title").a.text.strip()
print(title)

#存储数据
with open('title.txt', "a+") as f:
    f.write(title)
    f.close()
