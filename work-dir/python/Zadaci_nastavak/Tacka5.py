def draw_square(n, char='#'):
    if n <= 0:
        return
    for i in range(n):
        line = char * n  
        print(line)


print("Kvadrat sa stranicom od 5, koristeći #:")
draw_square(5)
print("\nKvadrat sa stranicom od 3, koristeći @:")
draw_square(3, '@')
print("\nKvadrat sa stranicom od 0:")
draw_square(0)
