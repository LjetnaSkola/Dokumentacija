def closure(tip):
    if(tip == "krug"):
        def circle(r):
            return r**2 * 3.14
        return circle
    elif (tip == "kvadrat"):
        def square(a):
            return a * a
        return square
    elif (tip == "pravougaonik"):
        def rectangle(a, b):
            return a * b
        return rectangle

def main():
    tip = "krug"
    r = 10
    print(closure(tip)(r))

    tip = "kvadrat"
    a = 5
    print(closure(tip)(a))

if __name__ == "__main__":
    main()
