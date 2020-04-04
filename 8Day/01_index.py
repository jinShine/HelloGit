from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
   return 'This is Home!'

@app.route('/mypage')
def my_page():
    return 'my page'

@app.route('/index')
def index():
    return render_template('index.html')

if __name__ == '__main__':
   app.run('0.0.0.0',port=5000,debug=True)