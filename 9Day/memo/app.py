from flask import Flask, render_template, jsonify, request
from bs4 import BeautifulSoup
from pymongo import MongoClient
import requests


app = Flask(__name__)

client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta                      # 'dbsparta'라는 이름의 db를 만듭니다.


## HTML을 주는 부분
@app.route('/')
def home():
   return render_template('/index.html')

@app.route('/memo', methods=['GET'])
def listing():
    # 1. 모든 document 찾기 & _id 값은 출력에서 제외하기
    articles = list(db.articles.find({}, {'_id': False}))
    
    # 2. articles라는 키 값으로 영화정보 내려주기
    return jsonify({
        'result':'success',
        'msg':'GET 연결되었습니다!',
        'articles':articles
    })

## API 역할을 하는 부분
@app.route('/memo', methods=['POST'])
def saving():
		# 1. 클라이언트로부터 데이터를 받기
        posting_url = request.form['posting_url']
        posting_comment = request.form['posting_comment']

        print(posting_url, posting_comment)
        
		# 2. meta tag를 스크래핑하기
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
        data = requests.get(posting_url, headers=headers)
        soup = BeautifulSoup(data.text, 'html.parser')

        og_image = soup.select_one('meta[property="og:image"]')
        og_title = soup.select_one('meta[property="og:title"]')
        og_description = soup.select_one('meta[property="og:description"]')

        article = {
            'url': posting_url,
            'comment': posting_comment,
            'image': og_image['content'],
            'title': og_title['content'],
            'desc': og_description['content']
        }

        print(article)
        db.articles.insert_one(article)

        return jsonify({'result': 'success', 'msg':'POST 연결되었습니다!'})
		# 3. mongoDB에 데이터 넣기

if __name__ == '__main__':
   app.run('0.0.0.0',port=5004,debug=True)