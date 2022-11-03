#!/usr/bin/python3
import flask
from flask import Flask, request, jsonify, make_response, abort
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

app.config['JSON_SORT_KEYS'] = False


details = {'slackUsername': 'Nikky',
     'backend': True,
     'age': 28,
     'bio': 'Nikki was born in Lagos in 1994'}

slackUsername = 'Nikky'



@app.route("/", methods=['GET'], strict_slashes=False)
def home():
    """Displays Welcome!"""
    return "Welcome To my Site!"

@app.route('/api/v1/detail', methods=['GET'])
def api_all():
    return jsonify(details)


@app.route('/api/v1/operations', methods=['POST'], strict_slashes=False)
def api_ops():
    temp = request.get_json()

    if not request.get_json():
        abort(400, description='Not a JSON')
    if 'operation_type' not in temp:
        abort(400, description='Missing operation_type')
    if 'x' not in temp:
        abort(400, description='Missing x')
    if 'y' not in temp:
        abort(400, description='Missing y')

    X = request.get('x')
    Y = request.get('y')
    operation_type = request.get('operation_type')
    

    if operation_type == 'addition':
        temp =  X + Y
    elif operation_type == 'subtraction':
        temp = X - Y
    elif operation_type == 'multiplication':
        temp = X * Y
    res = ['temp', 'slackUsername', 'operation_type']
    data = {}
    for m in res:
        if m == 'temp':
            data['temp'] = temp
        elif m == 'slackUsername':
            data['slackUsername'] = slackUsername
        elif m == 'operation_type':
            data['operation_type'] = operation_type

    return make_response(jsonify(data), 200)

if __name__ == '__main__':
    app.run()

