# -----------------------------------------------------------------------------
# API + MongoDB
# -----------------------------------------------------------------------------

from flask import Flask
from flask import render_template # laod HTML
from flask import request # GET, POST
from flask import jsonify # JSON형식으로 API를 만들어줌

from pymongo import MongoClient

# setup Flask
app = Flask(__name__)

# setup MongoDB
client = MongoClient('localhost', 27017)
db = client.product


@app.route('/')
def home():
    return render_template('review.html')

@app.route('/reviews', methods=['POST'])
def write_review():
    title = request.form['title_given']
    author = request.form['author_given']
    review = request.form['review_given']
    print(title, author, review)

    review = {
        'title': title,
        'author': author,
        'review': review
    }
    
    db.reviews.insert_one(review)

    send_msg = {
        'result': 'success',
        'msg': '리뷰가 성공적으로 작성되었습니다.'
    }
    
    return jsonify(send_msg)

@app.route('/reviews')
def read_review():
    reviews = list(db.reviews.find({}, {'_id':0}))
    send_msg = {
        'result': 'success',
        'reviews': reviews
    }
    return jsonify(send_msg)

if __name__ == '__main__':  
   app.run('0.0.0.0',port=5002,debug=True)
