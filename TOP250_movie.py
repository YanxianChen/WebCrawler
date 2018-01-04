import requests
from bs4 import  BeautifulSoup

def get_top250():
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
        'Host': 'movie.douban.com'
    }
    movie_list = []
    for i in range(10):
        link = 'https://movie.douban.com/top250?start=' + str(i * 25)
        response = requests.get(link, headers = headers, timeout = 20)
        print (str(i+1), '页响应状态码:', response.status_code)

        soup = BeautifulSoup(response.text, 'html')
        div_list = soup.find_all('div', class_ = 'hd')
        for each_movie in div_list:
            movie = each_movie.a.span.text.strip()
            movie_list.append(movie)
    return movie_list

top250 = get_top250()
print(top250)


