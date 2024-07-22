import math


def area_calculator(shape):

    if shape == 'circle':
        def calculate_area(radius):
            return math.pi * radius * 2
        return calculate_area

    elif shape == 'square':
        def calculate_area(side):
            return side ** 2
        return calculate_area

    elif shape == 'rectangle':
        def calculate_area(length, width):
            return length * width
        return calculate_area

    else:
        raise ValueError("Shape unsupported.")


circle_area_func = area_calculator('circle')
square_area_func = area_calculator('square')
rectangle_area_func = area_calculator('rectangle')

circle_area = circle_area_func(5)
square_area = square_area_func(4)
rectangle_area = rectangle_area_func(6, 3)

print(f"Area of circle with radius 5: {circle_area:.2f}")
print(f"Area of square with side 4: {square_area}")
print(f"Area of rectangle with length 6 and width 3: {rectangle_area}")
