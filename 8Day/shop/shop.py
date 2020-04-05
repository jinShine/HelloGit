# -*- coding: utf-8 -*- 

from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient

# setup mongoDB
client = MongoClient('localhost', 27017)
db = client.shop

# setup flask
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('order.html')

@app.route('/order', methods=['POST'])
def item_order():
    orderer = request.form['orderer']
    quantity = request.form['quantity']
    address = request.form['address']
    phone = request.form['phone']

    send_msg = {
        'result': 'success',
        'msg': '주문 완료',
    }

    db.orders.insert_one({
        'orderer': orderer,
        'quantity': quantity,
        'address': address,
        'phone': phone
    })

    return jsonify(send_msg)

@app.route('/order')
def load_item():
    orders_item = list(db.orders.find({},{'_id': 0}))
    print(orders_item)
    
    send_msg = {
        'result': 'success',
        'orders_item': orders_item
    }

    return jsonify(send_msg)

if __name__ == '__main__':
    app.run('0.0.0.0', port=5017, debug=True)