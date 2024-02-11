# numbers

# PEMDAS
print(5 * 5 + 5)
print(5 * ( 5+ 5))

# mod
print(100 % 24)

my_num = 8
print(my_num)

print(str(my_num) + "this will print")
# print(my_num + "this wont")

print(abs(-62))

print(pow(3, 3))

print(max(1,2,3,4,5))

print(min(1,2,3,4,5))

print(round(47.60))

from math import *
print(sqrt(36))
print(floor(3.6))
print(ceil(3.3))

import math
print(math.floor(3.6))

# bitwise vs. boolean
a = 0 < 1 & 0 < 2 # a = 0 < (1 & 0) < 2, ==== 0 < 0 < 2
b = 0 < 1 and 0 < 2
print(a)
print(b)