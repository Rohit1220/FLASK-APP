from flask import Flask
import flask
from requests import request
from flask.json import jsonify

tasks = [
    {
        'id':1,
        'title':'my books',
        'description':'chemistry, physics, Biology',
        'done':False
    }
]
@flask.route("/add-data",methods = ["POST"])
def  add_task():
    if not request.json:
        return jsonify({
            'status':'error',
            'message':'Please provide data',
        },400)

if (__name__ == "__main__"):
    flask.run(debug= True)