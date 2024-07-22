def draw_square(size, char="#"):
    for _ in range(size):
        for __ in range(size):
            print(char, end="")
        print()


if __name__ == "__main__":
    draw_square(4, "a")
    draw_square(5)
