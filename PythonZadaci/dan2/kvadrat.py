def draw(n, char = '#'):
    print(char*n)
    for i in range(0,n-2):
        print(char + " "*(n-2) + char)
    print(char*n)


def main():
    draw(6)
    
if __name__ == "__main__":
    main()
