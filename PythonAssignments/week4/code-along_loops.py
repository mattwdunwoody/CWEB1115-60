# for loops
for index in range(10):
    print(index)

for index in range(-1, 3):
    print(index)

superheros = ['Superheros', 'Batman', 'Catwoman']
for index in range(len(superheros)):
    print(superheros[index])

for index in range(5):
    if index == 0:
        print("This is the maiden voyage")
    else:
        print("You are beginning a new flight")

num_list = [1,2,3]
alpha_list = ['a', 'b', 'c']

for number in num_list:
    print(number)
    for letter in alpha_list:
        print('.........' + letter)

# while loop
# while a condition is true, loop

i = 1
while i <= 10:
    print(i)
    i += 1
print("done with loop")

# guessing game:
'''true_age = '29'
guess = ''

while guess != true_age:
   guess = input("How old do you think I am?")
print("You win")'''

# guessing game 2
'''true_age = '29'
guess = input('How old do you think I am?')
guess_count = 0
guess_limit = 4
out_of_guesses = False

while guess != true_age and not out_of_guesses:
    if guess_count < guess_limit:'''
        # always shows 4 guesses left.
'''
        guess = input('Try again. How old do you think I am? You have ' + str(guess_limit) + " more guesses. ")
        guess_count += 1
    else:
        out_of_guesses = True
        if out_of_guesses:
            print("Out of guesses; you lose!")
            break
else:
    print("You win")'''

# my version
true_age = '29'
guesses_left = 4
guess = input("How old do you think I am? ")

while(guess != true_age):
    guesses_left -= 1
    if(guesses_left < 1):
        print("Out of guesses, you lose!")
        break
    guess = input('Try again. How old do you think I am? You have ' + str(guesses_left) + " more guess(es). ")
else:
    print("You win!")

# nested while loop
i = 1
while i <= 3:
    print(i, 'outer loop is executed')
    j = 1
    while j <= 3:
        print(j, '____innter loop is executed')
        j+=1
    i += 1

# infinite loop
number = 0
while True:
    print(number)
    number += 1
    if number > 5000:
        break

# nested list
number_grid = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0]
]

print(number_grid[0][0])

for row in number_grid:
    print(row)
for row in number_grid:
    for col in row:
        print(col)