#!/usr/bin/python3

from flask import Flask, request, url_for, redirect, jsonify, make_response, abort, render_template
from flask_cors import CORS
from flask import flash
from dotenv import load_dotenv
from os import  environ

load_dotenv()
app = Flask(__name__)
CORS(app)

app.config['JSON_SORT_KEYS'] = False
app.config['SECRET_KEYS'] = environ.get('MY_SECRET_KEYS')




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


@app.route('/api/v1/operations', methods=[ 'POST'], strict_slashes=False)
def api_ops():
    if request.method == 'POST':
        temp = request.get_json()

        if not request.get_json():
            abort(400, description='Not a JSON')
        if 'operation_type' not in temp:
            abort(400, description='Missing operation_type')
        if 'x' not in temp:
            abort(400, description='Missing x')
        if 'y' not in temp:
            abort(400, description='Missing y')

        X = temp.get('x')
        Y = temp.get('y')
        operation_type = temp.get('operation_type')
        
        
        if operation_type == 'addition':
            result =  X + Y
        elif operation_type == 'subtraction':
            result = X - Y
        elif operation_type == 'multiplication':
            result = X * Y

        
        data = {}

        data['slackUsername'] = slackUsername
        data['result'] = result
        data['operation_type'] = operation_type
        

        return make_response(jsonify(data), 200)
    else:
        abort(400, description='Not a Vaild Request')





if __name__ == '__main__':
    app.run()

