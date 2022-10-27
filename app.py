#!/usr/bin/python3
import flask
from flask import Flask, request, jsonify
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

app.config['JSON_SORT_KEYS'] = False


details = [
    {'slackUsername': 'Nikki',
     'backend': True,
     'age': 28,
     'bio': 'Nikki was born in Lagos in 1994'}
]


@app.route("/", methods=['GET'], strict_slashes=False)
def home():
    """Displays Welcome!"""
    return "Welcome To my Site!"

@app.route('/api/v1/details/all', methods=['GET'])
def api_all():
    return jsonify(details)


if __name__ == '__main__':
    app.run()

