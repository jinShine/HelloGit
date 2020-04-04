# -----------------------------------------------------------------------------
# Flask 기초
# -----------------------------------------------------------------------------


from flask import Flask
from flask import render_template

app = Flask(__name__)

# --------------------------------------------------------------
# route를 통해서 URL을 나눌수 있다.

@app.route('/')
def home():
    return "Hello, World"


@app.route('/mypage')
def my_page():
    return 'hello, My page'

# --------------------------------------------------------------
# render_template을 이용해서 HTML파일을 불러올수 있다.

@app.route('/render')
def renderDef():
    return render_template('index.html')


if __name__ == '__main__':  
   app.run('0.0.0.0',port=5010,debug=True)