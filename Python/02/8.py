import os

class IoT:
    register = []   # class attribute
    temp = 0
    
    def __init__ (self, serialNumber, idCloud):
        for i in IoT.register:
            if i == serialNumber:
                IoT.temp = 1
                raise Exception("Serial Number MUST BE UNIQUE")
        if IoT.temp == 0:
            IoT.register.append(serialNumber);
            self.serialNumber = serialNumber    # serialNumber is unique
            self.idCloud = idCloud
        else:
            print("serial number must be unique")
    
    def __str__(self): # IoT device info
        return "IoT Device info -> serialNumber=%s , idCloud=%s" % (self.serialNumber, self.idCloud)
    
    def fileWrite(self):
        file_path = os.getenv('TEXT_FILE_PATH_WRITE')
        if not file_path:
            raise Exception("Environment variable TEXT_FILE_PATH_WRITE IS NOT SET ")

        with open(file_path, 'a') as f:
            f.write(self.__str__() + '\n')

def fileRead():
    file_path = os.getenv('TEXT_FILE_PATH_READ')
    if not file_path:
        raise Exception("Environment variable TEXT_FILE_PATH_READ IS NOT SET ")
    
    devices = []
    with open(file_path, 'r') as f:
        for line in f.readlines():
            line = line.strip()  # Uklonimo whitespace i newline karaktere
            if line:
                trashInfo, usefulInfo = line.split("->")
                serialNumber, idCloud = usefulInfo.split(',')
                x, serialNumber = serialNumber.split('=')
                y, idCloud = idCloud.split('=')
                device = IoT(serialNumber, idCloud)
                devices.append(device)
    return devices
            
# Testing

device1 = IoT(1, 1001)
device2 = IoT(2, 1002)
device3 = IoT(3, 1003)
device4 = IoT(4, 1004)
device5 = IoT(5, 1005)
device6 = IoT(6, 1006)
device7 = IoT(7, 1007)

# Testing Exception state
# device8 = IoT(1, 0000).__str__()

device1.fileWrite()
device2.fileWrite()
device3.fileWrite()

devices = fileRead()

for i in devices:
    print(i.__str__())