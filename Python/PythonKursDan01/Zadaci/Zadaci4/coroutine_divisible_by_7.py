def nearest_divisible_by_7_coroutine():
    try:
        while True:
            num = (yield)
            if num is not None:
                remainder = num % 7
                if remainder == 0:
                    print(f"{num} is already divisible by 7.")
                else:
                    lower_bound = num - remainder
                    upper_bound = num + (7 - remainder)

                if (num - lower_bound) <= (upper_bound - num):
                    closest = lower_bound
                else:
                    closest = upper_bound

                print(f"The nearest number to {num} divisible by 7 is {closest}")

    except GeneratorExit:
        print("Coroutine closed.")


def number_generator(start, end):
    for i in range(start, end):
        yield i


gen = number_generator(10 ,30)
coroutine = nearest_divisible_by_7_coroutine()
next(coroutine)

for number in gen:
    coroutine.send(number)
