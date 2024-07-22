import os
from iot_uredjaj import IotDev
from unique_device_decorator import is_unique


def writeToFile(dev):
    @is_unique(dev)
    def __write(devIn):
        path_ = os.getenv("OUT_FILE")
        if not path_:
            print("Environment variable OUT_FILE not set.")
        with open(path_, "a") as file_:
            file_.write(str(devIn))

    __write(dev)


if __name__ == "__main__":
    writeToFile(IotDev("1233", 215))
