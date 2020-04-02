# -*- coding: utf-8 -*-

from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.test_db


db.users.insert_one({'name': '김승진', 'age': 30})
db.users.insert_one({'name': '박근정', 'age': 30})
db.users.insert_one({'name': '이동희', 'age': 30})
db.users.insert_one({'name': '김동현', 'age': 35})
db.users.insert_one({'name': '이재섭', 'age': 32})
