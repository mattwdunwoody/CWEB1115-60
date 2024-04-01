def recite_poem():
    print("We are learning in school")
    print("That python is cool")

recite_poem()

# working through a sequence, and then we call the function, jump to the function, and then return to sequence
print("line 1")
recite_poem()
print("line 4")

# parameters
def recite_personalized_poem(name, language):
    print(name + " is learning in school")
    print("that " + language + " is cool!")

recite_personalized_poem("Matt", "Java")
recite_personalized_poem("Bartholomew", "JavaScript")

def square(number):
    return number **2

# return value
print(square(9))

# no return value
def cube(num):
    num*num*num

print(cube(3))

# return value
def cube(num):
    return num*num*num

print(cube(3))

result = cube(3)
print("I can treat result like a variable after its calculation as {}".format(result))

def cube(num):
    return num*num*num
    print("this line of code will be ignored after the return statement")

print(cube(4))

# lambda functions, one-liner, inline functions
square_lambda_function = lambda number: number**2
print(square_lambda_function(9))

import math
print(math.sqrt.__name__)

# execute immediately
# contain certain expressions, but not statements

x = lambda a, b, c: a + b + c
print(x(5,6,2))

# closure
def pop(list): # enclosing function
    def get_last_item(my_list): # local, a closure remembers the value of enclosing scope
        return my_list[len(list) - 1]
    list.remove(get_last_item(list))
    return list

a = [1,2,3,4,5]
print(pop(a))
print(pop(a))
print(pop(a))
print(pop(a))

# decorator
from datetime import datetime

def log_datetime(func):

    def wrapper():
        print(f'Function: {func.__name__}\nRun on: {datetime.today().strftime("%Y-%m-%d %H:%M:%S")}')
        print(f'{"-"*30}')
        func()
    return wrapper

@log_datetime
def daily_backup():
    print("Daily backup job has finished.")

daily_backup()