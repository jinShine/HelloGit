# -----------------------------------------------------------------------------
# 웹스크래핑 결과를 DB를 가지고 find, update 연습해보기
# -----------------------------------------------------------------------------

from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.movie_db # Database
rank_collection = db.rank # collections

# 문제 1
# 어벤져스: 엔드게임'의 평점을 가져오기

avengers_movie = rank_collection.find_one({'title':'어벤져스: 엔드게임'})
avengers_star = avengers_movie.get('star')
print(avengers_star)

# # 문제 2
# # '어벤져스: 엔드게임'의 평점과 같은 평점의 영화 제목들을 가져오기

target_star_list = rank_collection.find({'star': avengers_star})

for target_star in target_star_list:
    print(target_star.get('title'))

# # 문제 3
# # '어벤져스: 엔드게임'의 평점과 같은 평점의 영화 제목들의 평점을 0으로 만들기
rank_collection.update_many({'star': avengers_star}, {'$set': {'star': '0'}})


# # 문제 4
# # 1~20등 까지 평균 구하기

movies = rank_collection.find()

def average_star(movies):
    sum_value = 0.0

    for movie in movies:
        if movie['rank'] > 20:
            break

        star = float(movie.get('star'))
        sum_value += star

    return (sum_value / 20)

print(average_star(movies))
