#!/usr/bin/python3
import re



text = input("Enter a command: ")



regex = r'(add|divide|multiply|subtract|minus|division|multiplication\
    |subtraction|addition) ([\d\.]+) .*? ([\d\.]+)'

matches = re.search(regex, text)



command = matches.group(1)

number1 = matches.group(2)

number2 = matches.group(3)



number1 = float(number1)

number2 = float(number2)





def process_command(command, num1, num2):

    if command == "add":

        return num1 + num2

    elif command in ["subtract", "minus"]:

        return num1 - num2

    elif command == "divide":

        return num1 / num2

    elif command == "multiply":

        return num1 * num2



    else:

        return "Invalid command"





result = process_command(command, number1, number2)

print(result)

