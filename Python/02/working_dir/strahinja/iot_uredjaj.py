class IotDev:
    def __init__(self, snum, uid):
        self.snum = snum
        self.uid = uid

    def __str__(self):
        return f"({self.snum},{self.uid})"


if __name__ == "__main__":
    r = IotDev("12399812", 112)
    print(r)
