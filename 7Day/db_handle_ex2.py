from pymongo import MongoClient  # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)

client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbusers  # 'dbusers'라는 이름의 db를 만듭니다.

# 삽입
db.users.insert_one({'name': 'jinnify', 'age': 30})  # 한개 삽입

# 찾기
all_users = list(db.users.find())

for user in all_users:
    print(user)
