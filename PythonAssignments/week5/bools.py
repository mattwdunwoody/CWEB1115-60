# Booleans

x = 2
y = 3-1

if x == y:
    print('equivalent')
else:
    print("not equivalent")
print(bool(x==y))

# lets try not equivalent
x = 6
y = 3-1

if x != y:
    print('not equivalent')
else:
    print("equivalent")
print(bool(x!=y))

x = 1
y = 3-1

if x > y:
    print(str(x) + " is greater than " + str(y))
else:
    print(x, " is not greater than ", y)
print(bool(x>y))

'''
AND
P   Q   P and Q
T   T   T
T   F   F
F   T   F
F   F   F

OR
P   Q   P or Q
T   T   T
T   F   T
F   T   T
F   F   F

NOT
P   not P
T   F
F   T

'''
# and condition
sunny_weather = True
beach_open = True

if(sunny_weather and beach_open):
    print("Let's go!")
else:
    print("Sad face.")

# or condition
ticket = True
concert_worker = True

if ticket or concert_worker:
    print("Music!")
else:
    print("Sad face.")

# not condition
license = True
under_16 = False

if license and not under_16:
    print("Pizza delivery run!")
else:
    print("Not qualified.")

# careful with return values. If both are true, returns last value.
x = 10
y = 100

print(x and y)
print(y and x)
print(x or y)
print(y or x)

# test with booleans being displayed
# booleans are a sub-type of integers in python
x = 0
y = 100

print(bool(x and y))
print(bool(y and x))
print(bool(x or y))
print(bool(y or x))

# True and False are constants
# True = 1
# False = 0

