#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
import requests
from bs4 import BeautifulSoup

link = '''https://api-zero.livere.com/v1/comments/list?callback=jQuery112409167777692145258_1515115423265&limit=10&repSeq=
3871836&requestPath=%2Fv1%2Fcomments%2Flist&consumerSeq=1020&livereSeq=28583&smartloginSeq=5154&_=1515115423267'''
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
    'Host': 'api-zero.livere.com'
}
response = requests.get(link, headers = headers)

json_data = json.loads(response.text)
comment_list = json_data['data']['comments']
for each_comment in comment_list:
    message = comment_list[each_comment]['content']
    print(message)
