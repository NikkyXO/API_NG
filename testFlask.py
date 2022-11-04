#!/usr/bin/python3
import requests
from flask import request
import json

if __name__ == '__main__':
        
        
        url1 = 'https://hng-api-app.herokuapp.com/api/v1/operations'
        url = 'http://127.0.0.1:5000/api/v1/operations'
        headers = {'Content-Type' : 'application/json', 'Accept': '*' }
        data = {'operation_type': 'addition', 
                'x': 5, 
                'y': 10 }
        data1 = {'operation_type': 'i will like to + 10 and 7 ', 
                'x': 5, 
                'y': 10 }
        r = requests.post(url, json=data, headers=headers)
        print(r.json())
        

        

        