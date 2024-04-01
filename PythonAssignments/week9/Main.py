# from Student import Student

# student1 = Student('Jimbo', 'Welding', 3.0, 'N')
# student2 = Student('Martha', 'Robotics', 3.9, 'N')

# print(student1.name, "is on honor roll?", student1.on_honor_roll())
# print(student2.name, "is on honor roll?", student2.on_honor_roll())

from Triangle import Triangle as t

class Main:

    def main():

        triangle1 = t.triangleType(6,7,8)
        print(triangle1)

        triangle2 = t.triangleType(6,7,8).lower()
        print(triangle2)

        triangle3 = t.triangleType(6,6,6).lower()
        print(triangle3)
        
        triangle4 = t.triangleType(6,7,6).lower()
        print(triangle4)

        triangle5 = t.triangleType(0,0,0).lower()
        print(triangle5)

        triangle6 = t.triangleType(-6,-7,-8).lower()
        print(triangle6)

        triangle7 = t.triangleType(5,3,8).lower()
        print(triangle7)

    if __name__ == '__main__':
        main()