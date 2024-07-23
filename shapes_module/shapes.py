from math import pi

class Shapes:
    @staticmethod
    def square_area(height, width):
        return height * width
    
    @staticmethod
    def square_perimeter(height, width):
        return 2 * (height + width)
    
    @staticmethod
    def rectangle_area(height, width):
        return height * width
    
    @staticmethod
    def rectangle_perimeter(height, width):
        return 2 * (height + width)
    
    @staticmethod
    def circle_area(radius):
        return radius ** 2 * pi
    
    @staticmethod
    def circle_perimeter(radius):
        return 2 * radius * pi
    
    @staticmethod
    def triangle_area(height, base):
        return 0.5 * height * base
    
    @staticmethod
    def triangle_perimeter(a, b, c):
        return a + b + c

