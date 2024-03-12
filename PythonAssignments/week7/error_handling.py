# error handling in Python

# number = int(input("Enter a number: "))
# print(number)

# try:
#     number = int(input("Enter a number: "))
#     print(number)
# except ValueError as err:
#     print(err)

# try:
#     number = int(input("Enter a number: "))
#     print(number)
# except ValueError:
#     print("Hey, enter a number!")

# being general is not best practice
# try:
#     number = int(input("Enter a number: "))
#     print(number)
# except ValueError:
#     print("Hey, enter a number!")

# try:
#     number = eval(input("Enter a number divided by another number: "))
#     print(number)
# except ZeroDivisionError as err:
#     print("Hey, don't divide by 0")

# school_id = 0

# try:
#     if school_id < 200:
#         print(school_id)
# except:
#     print("we need a number, not a name!")
# finally:
#     print("School rocks!")

'''
try - try this code
except - do this if this exception is raised
except - do this if this exception is raised
... - might be more
else - optional, do this if we don't have any exceptions
finally - optional, do this no matter what
'''

def integer_test(test_int):
    x = int(test_int)
    y = x * 2
    return y

# try:
#     z =integer_test('hello')
#     print(z)
# except NameError as err:
#     print(err)
# except ValueError as err:
#     print(err)
# except (SyntaxError, TypeError):
#     print("you need to enter numbers.")
# else:
#     print("no exception")
# finally:
#     print("Done")

# demo of raising your own exception
try:
    z = 100
    if z == 20:
        raise ValueError
except ValueError:
    print("We don't want 20!")