office_supplies = {"sticky notes", "pens", "pencils", "tape", "staples"}
print(id(office_supplies))
print(office_supplies)

mixed_set = {"100", "erasers", 39, False}
print(mixed_set)

office_supplies = {"sticky notes", "pens", "pens", "tape", "tape"}
print(office_supplies)
print(id(office_supplies))

# you can add items without changing memory address
office_supplies.update(mixed_set)
print(office_supplies)
print(mixed_set)
print(id(office_supplies))
print(id(mixed_set))

veggies = ["artichoke", "arulgula", "beet"]
print(veggies[1])
print(veggies[-1])
print(veggies[1:])
print(veggies[0:1])
print(veggies[:2])
print(veggies[:3])
print(id(veggies))
veggies[0] = "Bok Choy"
print(veggies)
print(id(veggies))

#fruit = ("banana", "apple", "strawberry")
fruit = ["banana", "apple", "strawberry"]
veggies.extend(fruit)
print(veggies)
veggies.append("grape")
print(veggies)
# veggies.pop()
# veggies.pop()
veggies.pop(3)
print(veggies)
veggies.insert(2, "endive")
print(veggies)
veggies.remove("apple")
print(veggies)
# will error if not found
# print(veggies.index("test"))
veggies.append("Wonder Woman")
veggies.append("Wonder Woman")
print(veggies)
veggies.append("potato")
veggies.append("potato")
veggies.append("potato")
veggies.append("potato")
print(veggies.count("potato"))
veggies.sort()
print(veggies)
veggies_copy = veggies.copy()
print(veggies_copy)
veggies.clear()
print(veggies)

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

print(monthConversions.get("Dec", "not a value for this key"))

print(monthConversions.get("phone", "not a value for this key"))

dice_rolls = (3, 6, 9)
print(dice_rolls)

dice_roll_plays = [(3, 6, 9), (8, 9), (3, 4, 10, 2)]
print(dice_roll_plays)

dice_roll_plays.pop()
dice_roll_plays.pop()
dice_roll_plays.pop()

print(dice_roll_plays)