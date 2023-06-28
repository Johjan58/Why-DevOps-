"""/*A function is a block of code which only runs when it is called.
You can pass data, known as parameters, into a function.
A function can return data as a result. /*
Information can be passed into functions as arguments.

Arguments are specified after the function name, inside the parentheses. You can add as many arguments as you want, just separate them with a comma.
"""

def myfunction(name):
    print(name + " can you be my girlfriend?")

myfunction("sara")

"""
Lambda functiosns
A lambda function is a small anonymous function.
Why Use Lambda Functions?
The power of lambda is better shown when you use them as an anonymous function inside another function.
Say you have a function definition that takes one argument, and that argument will be multiplied with an unknown number:"""

def myfunction(n):
    return lambda a : a * n
mydoubler = myfunction(2)
print(mydoubler(11))
