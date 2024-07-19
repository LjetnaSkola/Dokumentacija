def nearest_divisible_by_7():
    generatorInput = yield
    try:
        i = next(generatorInput)
        while i is not None and i % 7 != 0:
            i = next(generatorInput)
        yield i
    except StopIteration as e:
        raise e


if __name__ == "__main__":
    coroutine = nearest_divisible_by_7()

    try:
        i = next(coroutine)
        print(coroutine.send(iter(range(100, 107))))
    except StopIteration:
        print("Not found in sequence")
