import os
from iot_uredjaj import IotDev


def readFromFile():
    path_ = os.getenv("OUT_FILE")
    if not path_:
        print("Environment variable OUT_FILE not set.")
    with open(path_, "r") as file_:
        devs = file_.read().split("(")

    iot_devs = [
        IotDev(snum.strip(), uid.strip())
        for dev in devs
        if dev.strip()
        for snum, uid in [dev.rsplit(")", 1)[0].split(",", 1)]
    ]

    return iot_devs


if __name__ == "__main__":
    for dev in readFromFile():
        print(dev)
