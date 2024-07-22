import os
class IoTDevice:
    def __init__(self,serial_number, cloud_id):
        self.serial_number = serial_number
        self.cloud_id = cloud_id
    def __str__(self):
        return f"{self.serial_number},{self.cloud_id}"
    
def write_devS_to_file(IoTDevice, env_path):
    '''
    This function writes all IoT devices to file
    '''
    file_loc = os.getenv(env_path)  
    if file_loc:
        #file_path = os.path.join(file_loc, 'iot_devices.txt')
        with open(file_loc, 'a') as f:
            f.write(str(IoTDevice) + '\n')
    else:
        print("Error - environment variable not set!")

def read_devS_from_file(env_path):
    '''
    This function reads all IoT devices from file into memory.
    Returns a list of IoTDevice objects.
    '''
    file_loc = os.getenv(env_path)  
    if file_loc:
        devices = []
        try:
            with open(file_loc, 'r') as f:
                for line in f:
                    serial_number, cloud_id = line.strip().split(',')
                    devices.append(IoTDevice(serial_number, cloud_id))
            return devices
        except FileNotFoundError:
            print(f"File {file_loc} not found.")
            return []
    else:
        print("Error - environment variable not set!")
        return []

        
    
def main():

    device1 = IoTDevice("SN001", "CID001")
    device2 = IoTDevice("SN002", "CID002")
    print("Serial number:", device1.serial_number)
    print("Cloud ID:", device1.cloud_id)
    print("Serial number:", device2.serial_number)
    print("Cloud ID:", device2.cloud_id)

    os.environ["DEV_FILE_PATH"] = "iot_devices.txt"
    write_devS_to_file(device1,"DEV_FILE_PATH")
    write_devS_to_file(device2,"DEV_FILE_PATH")
    devices = read_devS_from_file("DEV_FILE_PATH")
    print("\nDevices read from file:")
    for dev in devices:
        print(dev.serial_number, dev.cloud_id)

if __name__ == "__main__":
    main()