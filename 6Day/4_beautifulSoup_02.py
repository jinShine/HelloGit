import requests
from bs4 import BeautifulSoup

target_url = 'https://www.genie.co.kr/chart/top200?ditc=D&rtm=N&ymd=20200309'

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
response_data = requests.get(target_url, headers = headers)

response = BeautifulSoup(response_data.text, 'html.parser')

music_list = response.select('div.newest-list > div.music-list-wrap > table > tbody > tr')

for music in music_list:
    rank = music.select_one('td.number').get_text(separator=' ', strip=True).split(' ')[0]
    title = music.select_one('td.info > .title').get_text(strip=True)
    artist = music.select_one('td.info > .artist').get_text(strip=True)
    print(rank, title, artist)
