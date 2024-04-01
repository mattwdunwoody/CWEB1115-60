# source code from geeks for geeks https://www.geeksforgeeks.org/dont-forget-edge-cases/

class Triangle:

    # Check if given sides form a triangle or not
    def triangleValidator(side1, side2 , side3):
        
        if side1 <= 0 or side2 <= 0 or side3 <= 0:
            return False
            
        elif (side1 + side2 >= side3) and\
            (side2 + side3 >= side1) and\
            (side3 + side1 >= side2):
            return True
        return False

    # Return the type of triangle
    def triangleType(side1, side2, side3):
        
        # If not a triangle, return "Not a triangle"
        if Triangle.triangleValidator(side1, side2, side3) == False:
            return "Not A Triangle"
            
        # Else perform type checking
        if side1 == side2 == side3:
            return "Equilateral Triangle"
            
        elif (side1 == side2) or\
            (side2 == side3) or\
            (side3 == side1):
            return "Isosceles Triangle"
            
        return "Scalar Triangle"