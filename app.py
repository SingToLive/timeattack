from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient
import hashlib
import certifi  #만약 몽고 디비 돌릴때 문제가 없으셨다면 해당 줄은 주석 처리 하세요.
client = MongoClient(')
db = client.dbsparta
app = Flask(__name__)

@app.route('/')
def login():
    return render_template('home.html')

@app.route('/signup', methods=['POST'])
def signup():
    email = request.form["email"]
    password = request.form["password"]

    pass_ch = hashlib.sha256(password.encode('utf-8')).hexdigest()

    doc = {'email':email, 'password':pass_ch}

    db.timeattack.insert_one(doc)
    print(doc)
    return jsonify()

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)