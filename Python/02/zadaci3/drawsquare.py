def char_squared(n, character = '#'):
    for i in range(n):
        if i == 0 or i == n - 1:
            print(character * n)
        else:
            print(character + ' ' * (n - 2) + character)
def main():
    # If not given, by default it uses #
    char_squared(5)
    # Prints given output character
    char_squared(4, '@')


if __name__ == "__main__":
    main()
