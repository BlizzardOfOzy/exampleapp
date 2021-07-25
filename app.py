from flask import Flask, request, render_template, redirect, url_for
from flask import json
from flask.json import jsonify
from pymongo import MongoClient
from bson import json_util

app = Flask(__name__)

client = MongoClient(host='mongo-mongodb-headless')
database = client.database

@app.route("/", methods=['POST'])
def put_record():
    new_data = dict(request.form)
    database.example.insert_one(new_data)
    return redirect(url_for('get_record'))

@app.route("/", methods=['GET'])
def get_record():
    return render_template('index.html', data=json_util.dumps({'records': list(database.example.find({}))}))
        