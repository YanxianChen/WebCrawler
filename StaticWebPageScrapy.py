#!/user/bin/python
# coding: UTF-8

import requests

link = 'http://www.santostang.com/'
headers = {
    'Connection': 'keep-alive',
    'Host': 'www.santostang.com',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
}
key_dict = {'key1': 'value1', 'key2': 'value2'}
response = requests.get(link, headers = headers)
print('文本编码:', response.encoding)
print('状态响应码:', response.status_code)




