# filtering with list
letter = "J"
friend_list = ['Michael', 'Jim', 'Pam', 'Kelly', 'Stanley', 'Dwight']

for i in friend_list:
    if i.startswith(letter):
        print(i)

print(', '.join([i for i in friend_list if i.startswith(letter)]))

actor_list = ['Steve', 'John', 'Jenna', 'Mindy', 'Leslie', 'Rainn']

casting = list(zip(actor_list, friend_list))
print(casting)

# we could insert this list of tuples into a table, likely with keys
# sql = "INSERT INTO casting (actor, role) VALUES (%s, %s)"
# val = casting
# mycursor.executemany(sql, val)
# mydb.commit()

original_list = [1,2,3,4,5]
reversed_list = original_list[::-1]
print(reversed_list)

if 5 in original_list:
    print('yes')
else:
    print('no')

programs = ['IENG', 'MENG', 'SENG', 'EENG', 'EENG']
majors = set(programs)
print(majors)

print(max(programs, key = programs.count))

x = [True, True, False]
if any(x):
    print("at least one is true.")
if all(x):
    print("all of x is true.")
if any(x) and not all(x):
    print("at least one true and one false.")

dunwoody = ['born', 'to', 'do']
print('born' in dunwoody)
print('nothing' in dunwoody)

from  itertools import combinations
comb = combinations([1,2,3], 2)
for i in list(comb):
    print("combos: ", i)

from itertools import permutations
perm = permutations([1,2,3], 2)
for i in list(perm):
    print("perms: ", i)

A = {1,2,3,4,5}
B = {2,4,6,8}

print(A.union(B))
print(A|B)

A = {1,2,3,4,5}
B = {2,4,6,8,10}
C = {1,3,5,7,9}

print(A|B|C)
print(A.union(B,C))

A = {1,2,3,4,5}
B = {2,4,6,8}

print(A.intersection(B))
print(A&B)

A = {1,2,3,4,5}
B = {2,4,6,8,10}
C = {2,4}

print(A.intersection(B,C))
print(A&B&C)

print(A.difference(B))
print(A-B)
print(B.difference(A))
print(B-A)
