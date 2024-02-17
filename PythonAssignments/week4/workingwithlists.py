########### Instructions.#######################
# Write a program to determine the prime numbers within a list using two coding approaches, 
# 1. list comprehension, and 2. a nested for loop. 
# Start by defining a function for each of the above.
# Both should find the prime numbers within the range of numbers.
# The range is 2 through a number provided as a parameter.
# Print the results returned from both functions. The results should be the same.

########### Here are the results of providing the actual parameter of 100 as the top of the range. #######################
# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

########### Pseudocode.#######################
# Define the first of two functions taking in a parameter that will be the top of the range.
#   return the result of a list using list comprehension in one line. return [i for i in range(2, x) if a certain condition is met]

# Define the second of two functions taking in a parameter that will be the top of the range.
#   Create an empty list and assign to a variable.
#   Use a for loop to iterate the range.
#       Use a nested for loop to iterate up to the square root of the parameter that is the top of the range.
#           If the formula for determining a prime number reveals the number is not a prime number, then break.
#       Otherwise (else), append the number to the prime number list.
#   return the prime number list.

# Call the first function and print the result of the 1st function.
# Call the second function and print the result of the second function.

########### Hints.#######################
# Add 1 to the number of the actual parameter provided, as the range is only up to, but not including, the end number).
# A number to the power of 0.5 is the same thing as using math.sqrt.
# If we can't find any factors less than or equal to the square root of n, n must be a prime number. So, 9 divided by 3 = 3 so it is not prime.
#   I.e., 9 divided by 3 leaves a remainder of 0 and is not a prime number. 7 divided by its square root (7 ** 0.5) has a remainder that is not 0, 
#       and it is a prime number.
# With some blank lines, these instructions are 35 lines long. The candidate solution code is 16 lines long, with 3 blank lines included. 
#   There is more than one way to code this correctly.

from math import sqrt, ceil

def primeComprehension(user_range):    
    prime_list = [ number for number in range(2, user_range+1) if all(number % factor != 0 for factor in range(2, ceil(sqrt(number))+1)) ]
    return prime_list
 
def primeForLoop(user_range):
    prime_list = []
    for number in range(2, user_range+1):
        prime = True
        for factor in range(2, ceil(sqrt(number))+1):
            if(number % factor == 0): prime = False
        if(prime): prime_list.append(number)
    return prime_list

user_range = int(input("please enter the range: "))
print(str(primeComprehension(user_range))+"\n"+str(primeForLoop(user_range)))