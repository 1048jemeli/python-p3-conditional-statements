#!/usr/bin/env python3

def admin_login(username, password):
    if username.lower() == "admin" and password == "12345":
        return "Access granted"
    else:
        return "Access denied"

def hows_the_weather(temperature):
    if temperature < 0:
        return "It's freezing out!"
    elif 0 <= temperature <= 10:
        return "It's quite cold."
    elif 11 <= temperature <= 20:
        return "It's a bit chilly."
    elif 21 <= temperature <= 30:
        return "The weather is nice."
    elif 31 <= temperature <= 40:
        return "It's brisk out there!"
    elif 41 <= temperature <= 60:
        return "It's a little chilly out there!"
    elif 61 <= temperature <= 85:
        return "It's perfect out there!"
    else:
        return "It's too dang hot out there!"

def fizzbuzz(num):
    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return num  

def calculator(operation, num1, num2):
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero"
    else:
        print("Invalid operation!")
        return None

if __name__ == "__main__":
    print(admin_login("admin", "12345"))  
    print(hows_the_weather(15))          
    print(fizzbuzz(15))                  
    print(calculator("add", 10, 5))     
    print(calculator("divide", 10, 0))   
