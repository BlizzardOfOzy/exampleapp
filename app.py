from flask import Flask, request
from flask import json
from flask.json import jsonify
from pymongo import MongoClient
from bson import json_util

app = Flask(__name__)

client = MongoClient(host='192.168.33.10:27017')
database = client.database

@app.route("/", methods=['PUT'])
def put_record():
    database.example.insert_one(request.json)
    return "Success"

@app.route("/", methods=['GET'])
def get_record():
    return json_util.dumps({'records': list(database.example.find({}))})