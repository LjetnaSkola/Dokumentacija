# Defining closure function to calculate area of circle, square or rectangle
def outer_function():
    def circle_area(radius):
        return pow(radius,2)*3.14
    def square_area(length):
        return pow(length,2)
    def rect_area(length,width):
        return length*width
    return circle_area,square_area,rect_area

circle_area_func, square_area_func, rectangle_area_func = outer_function()

print("Circle area : ", circle_area_func(2.5))
print("Square area : ", square_area_func(5))
print("Rectangle area : ", rectangle_area_func(5,2.5))