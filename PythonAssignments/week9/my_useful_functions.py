# These are functions we can build ourselves to use in other files.
# These are beyond the modules built into Python, and those external modules we can install.

# Create 5 functions of your own. Here are two function examples.

#We might want to grab the file extension of a file.
def get_file_ext(filename):
    return filename[filename.index(".") + 1:]

# We get a random dice roll returned in this function.
# We will leverage a built-in Python module, random in this function.

import random
def roll_dice(num):
    return random.randint(1, num) # return a random int between this min and max

def add_numbers(x, y):
    return x + y

def subtract_numbers(x, y):
    return x - y

def square_number(x):
    return x**2

def square_root(x):
    return x**0.5

def add_smiley(user_string):
    return user_string + " :)"