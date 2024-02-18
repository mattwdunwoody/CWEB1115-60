# decision structures
# respond to conditions or events

'''
If class is scheduled for today
I get up early and go to class

If class is not scheduled for today
I sleep in
'''

class_today = True

print(type(class_today))

if class_today:
    print("get up and go to class")
else:
    print("zzzzzzzzzz")

active_session = True
class_today = True

if class_today and active_session:
    print("get up and go to class")
elif not class_today and active_session:
    print("zzzzzzzzzz")
elif not class_today and not active_session:
    print("Do whatever you want.")
else:
    print("something is not right, how can there be a class when school is not in session?")


active_session = True
class_today = True

if class_today and active_session:
    print("get ready")
    print("get up and go to class")
elif not class_today and active_session:
    print("turn off alarm")
    print("zzzzzzzzzz")
elif not class_today and not active_session:
    print("Do whatever you want.")
else:
    print("something is not right, how can there be a class when school is not in session?")


# or operator
semester_7 = True
semester_8 = False

if semester_7 or semester_8:
    print("you should be working on your capstone")
else:
    print("semester 7 or 8 would be better to work on your capstone.")

# determine highest number
def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3
    
print(max_num(23, 56, 87))

# strings
def match(emotion1, emotion2):
    if emotion1 == emotion2:
        return 'match'
    else:
        return 'no match'

print(match("happy", "sad"))

# != means not equal
if "this" != "that":
    print("this is not that")

# nested if statements
money = 50.00

if money >= 100.00:
    print("Get reimbursed")
    if money >= 1000.00:
        print("you can get reimbursed, but also get preapproval")
elif money < 100.00 and money != .01:
    print("Use petty cash")
else:
    print("Guess you dont need any money")


# use pass for dev/testing
money = 50.00

if money >= 100.00:
    print("Get reimbursed")
    if money >= 1000.00:
        pass
elif money < 100.00 and money != .01:
    print("Use petty cash")
else:
    print("Guess you dont need any money")

# switch
# case statements

# one line if statement
if money >= 100.00: print("get reimbursed")
# conditional expression (Python's ternary operator)

Senior = False
print("Are you graduating soon?", "Yes" if Senior == True else 'no')