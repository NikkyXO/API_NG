#!/usr/bin/python3
import flask
from flask import Flask, request, jsonify


app = Flask(__name__)
app.config['DEBUG'] = True
app.config['JSON_SORT_KEYS'] = False


details = [
    {'slackUsername': 'NikkyXO',
     'backend': 'Yes',
     'age': '29.',
     'bio': '1993'},
    {'slackUsername': 'Nikky',
     'backend': 'No',
     'age': '19.',
     'bio': '1998'},
    {'slackUsername': 'Amber',
     'backend': 'No',
     'age': '34',
     'bio': '1989'},
]


@app.route("/", methods=['GET'], strict_slashes=False)
def home():
    """Displays Welcome!"""
    return "Welcome To my Site!"

@app.route('/api/v1/details/all', methods=['GET'])
def api_all():
    return jsonify(details[0])

@app.route('/api/details/<string:name>', methods=['GET'])
def api_name(name):
    
    if 'name' in request.args:
        name = request.args['name']
    else:
        return "Error: No name field provided. Please specify an name."


    results = []

    for detail in details:
        if detail['name'] == name:
            results.append(detail)
    return jsonify(results)

if __name__ == '__main__':
    app.run()

