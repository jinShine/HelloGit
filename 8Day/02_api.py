# -----------------------------------------------------------------------------
# GET, POST
# -----------------------------------------------------------------------------

from flask import Flask
from flask import render_template # laod HTML
from flask import request # GET, POST
from flask import jsonify # JSON형식으로 API를 만들어줌

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/test', methods=['POST'])
def test_post():
    title = request.form['title_given']
    send_msg = {
        'result': 'success',
        'msg': {
            'title': title
        }
    }
    return jsonify(send_msg)

@app.route('/test')
def test_get():
    title = request.args.get('title_given')
    send_msg = {
        'result': 'success',
        'msg': {
            'title': title
        }
    }

    return jsonify(send_msg)

if __name__ == '__main__':  
   app.run('0.0.0.0',port=5002,debug=True)