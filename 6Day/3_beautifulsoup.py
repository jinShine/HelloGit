import requests
from bs4 import BeautifulSoup

# 타겟 URL을 읽어서 HTML를 받아오고,
html_data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20200303')

# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
# soup이라는 변수에 "파싱 용이해진 html"이 담긴 상태가 됨
# 이제 코딩을 통해 필요한 부분을 추출하면 된다.

# 첫번째 파라미터는 html소스코드, 두번째는 어떤 파서를 이용할지
soup = BeautifulSoup(html_data.text, 'html.parser')


# 여기까지가 기본 셋팅
###############################################################################################################


# 영화 순위, 제목, 별점 추가 해보기

movies = soup.select('#old_content > table > tbody > tr')

rank = 1
for movie in movies:
    title = movie.select_one('td.title > div.tit5 > a')
    point = movie.select_one('td.point')

    if title is not None:
        print(rank, title.text, point.text)
        rank += 1


# 결과값
# 1 그린 북 9.60
# 2 가버나움 9.59
# 3 베일리 어게인 9.52
# ...