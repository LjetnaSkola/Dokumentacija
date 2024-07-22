def korutina_najblizi_deljiv_sa_7():
    najblizi = None
    while True:
        broj = yield najblizi
        if broj % 7 == 0:
            if najblizi is None or abs(broj) > abs(najblizi):
                 najblizi = broj
            elif abs(broj) == abs(najblizi) and broj > najblizi:
                najblizi = broj

def generator_brojeva(od_broja, do_broja):
    for broj in range(od_broja, do_broja + 1):
        yield broj

od_broja = 10
do_broja = 100

generator = generator_brojeva(od_broja, do_broja)
korutina = korutina_najblizi_deljiv_sa_7()

next(korutina)  # Initialize the coroutine
while True:
    try:
        broj = next(generator)
        najblizi_djeljiv_sa_7 = korutina.send(broj)  # Capture the value sent by coroutine
    except StopIteration:
        break  # Exit loop if generator is exhausted

print("Najbliži broj koji je djeljiv sa 7 je:", najblizi_djeljiv_sa_7)

