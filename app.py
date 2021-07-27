from flask import Flask, request, render_template, redirect, url_for
from flask import json
from flask.json import jsonify
from pymongo import MongoClient
from bson import json_util
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
metrics = PrometheusMetrics(app)

client = MongoClient(host='mongo-mongodb-headless', replicaset='rs0')
database = client.database

@app.route("/", methods=['POST'])
def put_record():
    new_data = dict(request.form)
    database.example.insert_one(new_data)
    return redirect(url_for('get_record'))

@app.route("/", methods=['GET'])
def get_record():
    return render_template('index.html', data=json_util.dumps({'records': list(database.example.find({}))}))
        