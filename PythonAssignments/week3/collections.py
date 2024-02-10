superHeroes = ["Superman", "Catwoman", "Spiderman"]

# change how it is printed
print(superHeroes)
print(superHeroes[1])
print(superHeroes[-2])
print(superHeroes[1:])
print(superHeroes[0:2])
print(superHeroes[:3])

# modify data at index
superHeroes = ["Superman", "Catwoman", "Spiderman"]
superHeroes[0] = "Superwoman"
print(superHeroes)

# extend/append the list
superVillians = ["Dr. Doom", "Loki", "Green Goblin"]
superHeroes.extend(superHeroes)
print(superHeroes)

superHeroes.append("Wonder Woman")
print(superHeroes)

# test pop, pop removes data at a certain index
superHeroes.pop(3)
print(superHeroes)

# leaving pop empty will remove the last item in the list
superHeroes.pop()
print(superHeroes)

# items can be inserted with .insert()
superHeroes.insert(2, "Venom")
print(superHeroes)

# specified items can be removed with .remove()
superHeroes.remove("Venom")
print(superHeroes)

# .index() can be used to get the index of an item in a list
print(superVillians.index("Loki"))

superHeroes.append("Wonder Woman")
superHeroes.append("Wonder Woman")
print(superHeroes)

# .count() is case sensitive
print(superHeroes.count("Wonder Woman"))

superHeroes = ["Superman", "Catwoman", "Spiderman"]
superHeroes.sort()
print(superHeroes)

superHeroesCopy = superHeroes.copy()
print(superHeroesCopy)

print(superHeroes)
superHeroes.clear()
print(superHeroes)

# tuples
dice_rolls = (3, 6, 9)
print(dice_rolls)

# tuples are immutable
# dice_rolls[1] = 8

# tuples can not do pop
# dice_rolls.pop()
# print(dice_rolls)

# you can have a list of tuples
dice_roll_plays = [(3, 6, 9), (8, 9), (3, 4, 10, 2)]
print(dice_roll_plays)

# tuples support multiple data types
dice_rolls = (3, "giraffe", 9)
print(dice_rolls)

# dictionaries
monthConversions = {
    "Jan" : "January",
    "Feb" : "February",
    "Mar" : "March",
    "Apr" : "April",
    "May" : "May",
    "Jun" : "June",
    "Jul" : "July",
    "Aug" : "August",
    "Sep" : "September",
    "Oct" : "October",
    "Nov" : "November",
    "Dec" : "December"
}

print(monthConversions["Nov"])

print(monthConversions.get("Gir", "not a value key"))

# sets
# sets will normalize themselves, and you also can not order them

soft_drinks = {"Coke", "Pepsi", "Rootbeer", "Sunnkist", "Coke"}
print(soft_drinks)

mixed_set = {"Coke", "Pepsi", "Rootbeer", "Sunnkist", "Coke", 39, False}
print(mixed_set)

soft_drinks.update(mixed_set)
print(soft_drinks)