# validation checks
# assert
# unit test

# selection = input("choose a number between 1 and 10")
# print(selection)

# selection = int(input("Choose a number between 1 and 10."))
# if selection > 0 and selection < 11:
#     print(selection)
# else:
#     print("Hey, you need to read the instructions again!")
#     selection = int(input("Choose a number between 1 and 10."))
#     if selection > 0 and selection < 11:
#         print(selection)
#     else:
#         print("I give up on you!")

# you can also use the keyword "assert"
# selection = int(input("Choose a number between 1 and 10."))
# assert selection > 0 and selection < 11, "Hey you need to read the instructions a gain!"
# print(selection)

# unit tests

import unittest

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

if __name__ == '__main__':
    unittest.main()