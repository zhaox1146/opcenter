#-*- coding: utf-8 -*-
from flask import Flask, jsonify, render_template, request
app = Flask(__name__)
value = 'value'
name = 'name'
@app.route('/weather')
def weather():
    list = [11, 2, 3, 4, 5, 6]
    return jsonify(month=[x for x in list])
@app.route('/bing')
def huiyu():
    list = [{value:113,name:'aaa'},{value:222,name:'bbb'},{value:333,name:'ccc'}]
    return jsonify(data=[a for a in list])

@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)