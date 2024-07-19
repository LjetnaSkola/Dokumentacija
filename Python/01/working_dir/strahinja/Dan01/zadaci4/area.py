import math


def get_area_fn(shape):
    def area_circle(r):
        return math.pow(r, 2) * math.pi

    def area_square(a):
        return math.pow(a, 2)

    def area_rectangle(a, b):
        return a * b

    match shape:
        case "circle":
            return area_circle
        case "square":
            return area_square
        case "rectangle":
            return area_rectangle


if __name__ == "__main__":
    print(f"Circle with radius 3.14 has area of: {get_area_fn("circle")(3.14)}")
    print(f"While pi^3 is: {math.pow(math.pi, 3)}")

    print(f"Square with side 5 has area of: {get_area_fn("square")(5)}")

    print(f"Rectangle 4x5 has area of: {get_area_fn("rectangle")(4, 5)}")
