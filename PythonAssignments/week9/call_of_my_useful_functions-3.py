# we need to import our other file to use it here when we call our functions.
import my_useful_functions as m

# Now, call all five functions from the other file. Below, we are calling the two example functions and passing an input parameter in each case.

print(m.get_file_ext("document.docx"))
print(m.roll_dice(12))
print(m.add_numbers(2, 2))
print(m.subtract_numbers(5, 3))
print(m.square_number(10))
print(m.square_root(10))
print(m.add_smiley("Hello."))