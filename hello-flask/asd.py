# def add(n1, n2):
#     return n1 + n2
#
#
# def subtract(n1, n2):
#     return n1 - n2
#
#
# def multiply(n1, n2):
#     return n1 * n2
#
#
# def divide(n1, n2):
#     return n1 / n2
#
#
# def calculate(function, n1, n2):
#     return function(n1, n2)
#
#
# result = calculate(add, 2, 3)
# print(result)
#
#####################################################
#
# def outer_function():
#     print("I'm outer")
#
#     def nested_function():
#         print("I'm inner")
#
#     nested_function()
#
# outer_function()

#####################################################

# def outer_function():
#     print("I'm outer")
#
#     def nested_function():
#         print("I'm inner")
#
#     return nested_function
#
# inner_function = outer_function()
# inner_function()

#####################################################

import time

def delay_decorator(function):
    def wrapper_function():
        time.sleep(2)
        function()
        function()

    return wrapper_function

@delay_decorator
def say_hello():
    print("Hello")

@delay_decorator
def say_bye():
    print("Bye")

def say_greeting():
    print("How are you?")

decorated_function = delay_decorator(say_greeting)
decorated_function()

