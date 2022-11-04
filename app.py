#!/usr/bin/python3

from flask import Flask, request, url_for, redirect, jsonify, make_response, abort, render_template
from flask_cors import CORS
from flask import flash
from dotenv import load_dotenv
from os import  environ
import enum
import re

load_dotenv()
app = Flask(__name__)
CORS(app)

app.config['JSON_SORT_KEYS'] = False
app.config['SECRET_KEYS'] = environ.get('MY_SECRET_KEYS')


details = {'slackUsername': 'Nikky',
     'backend': True,
     'age': 27,
     'bio': 'Nikki was born in Lagos in 1995'}


slackUsername = 'Nikky'

@app.route("/", methods=['GET'], strict_slashes=False)
def home():
    """Displays Welcome!"""
    return "Welcome To my Site!"

@app.route('/api/v1/detail', methods=['GET'])
def api_all():
    return jsonify(details)

# Accessory Methods
class Operator(enum.Enum):
    addition = 'addition'
    subtraction = 'subtraction'
    multiplication = 'multiplication'



@app.route('/api/v1/operations', methods=[ 'POST'], strict_slashes=False)
def api_ops():
    if request.method == 'POST':
        temp = request.get_json()
        print(temp, 'temmmpppppp')
        if not request.get_json():
            abort(400, description='Not a JSON')
        if 'operation_type' not in temp:
            abort(400, description='Missing operation_type')
        if 'x' not in temp:
            abort(400, description='Missing x')
        if 'y' not in temp:
            abort(400, description='Missing y')
        data = {
            'slackUsername' : slackUsername,
            'operation_type' : '',
        }
        X = temp.get('x')
        Y = temp.get('y')
        
        operation_type = temp.get('operation_type')
        
        if len(operation_type.split()) > 1:
            tempList = operation_type.split(' ')
            numbers = []

            for op in tempList:
                if op in ['addition', 'add', 'sum', 'plus', '+', 'added']:
                    operation_type = 'addition'
                    
                elif op in ['sub', 'subtract', 'subtraction', 'minus', '-', 'subtracted']:
                    operation_type = 'subtraction'
                elif op in ['*', 'times', 'multiply', 'multiplication', 'multiplied']:
                    operation_type = 'multiplication'
            for m, op in enumerate(tempList):
                if  op.isdigit():
                    print(op)
                    numbers.append(op)
                else:
                    continue

            number1 = numbers[0]
            number1 = int(number1)
            number2 = numbers[1]
            number2 = int(number2)
            data['operation_type'] = operation_type

            if operation_type == "addition":
                result = number1 + number2
            elif operation_type == "subtraction":
                result = number1 - number2
            elif operation_type == "multiplication":
                result = number1 * number2
            else:
                return "No valid operation entered"
            
        
        elif len(operation_type.split()) == 1:
            if operation_type == Operator.addition.name:
                result =  X + Y
                data['operation_type'] = Operator.addition.value
            elif operation_type == Operator.subtraction.name:
                result = X - Y
                data['operation_type'] = Operator.subtraction.value
            elif operation_type == Operator.multiplication.name:
                result = X * Y
                data['operation_type'] = Operator.multiplication.value
        else:
            result = 'Enter Operation Type'

        data['result'] = result
        
        

        return make_response(jsonify(data), 200)
    else:
        abort(400, description='Not a Vaild Request')





if __name__ == '__main__':
    app.run()

