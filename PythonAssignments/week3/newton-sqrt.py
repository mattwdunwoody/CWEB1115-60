# Matthew Wideman
# CWEB1115-60 Programming
# Week 3 -> numbers
# Create an algorithm for computing square roots using Newton's method

import math

# defining method, x is the number to calculate the square root for, and i is the number of iterations to try
def newtonSqrt(x, i):

    # intialize the guess
    guess = x

    # iterate the formula as many times as given
    while(i > 0):

        # calculate the next closest guess
        guess = ((x/guess) + guess)/2

        # mark this iteration as done
        i -= 1
    
    # when all iterations are completed, return the calculated root
    return guess

# get input
num = int(input("Please enter a number to get the square root of: "))
iterations = int(input("Please enter the number of iterations to try: "))
calculatedSqrt = newtonSqrt(num, iterations)

# show output
print("The attempted square root for " + str(num) + " with " + str(iterations) + " iterations is: " + str(calculatedSqrt))
print("The actual square root of " + str(num) + " is " + str(math.sqrt(abs(num))))
print("The attempt was off by: " + str(abs(math.sqrt(abs(num))-calculatedSqrt)))

    