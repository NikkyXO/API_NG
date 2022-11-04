#!/usr/bin/python3
from flask import request
import re

# For Regex
ADDITION = ['addition', 'add', 'sum', 'plus', '+', 'added']
SUBTRACTION = ['sub', 'subtract', 'subtraction', 'minus', '-', 'subtracted']
MULTIPLICATION = ['*', 'times', 'multipy', 'multiplication', 'multiplied']

def translate_text(text):
    operations = ADDITION + SUBTRACTION + MULTIPLICATION
    text = re.sub(r'[^\w]', '', text)
    numbers = re.findall('[0-9]+', text)

    # remove all symbols then split
    textList = text.split()
    command = ''
    for a in textList:
        print(a)
        if a.lower() in operations:
            command = a
    number1 = numbers[0]
    number1 = int(number1)
    number2 = numbers[1]
    number2 = int(number2)
    return {'operation_type':command, 'x': number1, 'y': number2}

def translate_text1():

                # temp = request.get_json()
                temp = "i will like to multiply 5 and 7"
                tempList = temp.split(' ')
                numbers = []
                if len(tempList) > 1:
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

                        if operation_type == "addition":
                            result = number1 + number2
                        elif operation_type == "subtraction":
                            result = number1 - number2
                        elif operation_type == "multiplication":
                            result = number1 * number2
                        else:
                            print("No valid operation entered")
                        print(result)

print(translate_text1())



    
    


