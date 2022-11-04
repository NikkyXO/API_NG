#!/usr/bin/python3
import requests
import json

if __name__ == '__main__':
        
        
        url = 'http://127.0.0.1:5000/api/v1/operations'
        headers = {'Content-Type' : 'application/json', 'Accept': 'text/plain' }
        data = {'operation_type': 'addition', 
                'x': 5, 
                'y': 10 }

        r = requests.post(url, data=json.dumps(data), headers=headers)
        print(r.json())