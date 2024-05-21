#!/usr/bin/env python3

def admin_login(username, password):
    # your code here
    if username =='ADMIN' and password == "12345":
       return  'access'
    

    pass

def hows_the_weather(temperature):
    # your code here
    if temperature < 40 :
       return  "It's brisk out there!"
    elif 65 >= temperature >= 40 :
       return  "It's a little chilly out there!"
    elif temperature >= 85 :
        return "It's perfect out there!"

def fizzbuzz(num):
     if not num % 15:
        return "FizzBuzz"
     elif not num % 3:  
      return "Fizz"
     elif num % 5: 
      return "Buzz"
    
    # your code here
    

def calculator(operation, num1, num2):
    if operation == "+":
       return num1+num2
    if operation == "-":
      return num1-num2
    if operation == "*":
       return num1*num2
    if operation == "/":
       return num1/num2
    if operation == "none":
       return "Invalid operation!"
    # your code here
    pass
