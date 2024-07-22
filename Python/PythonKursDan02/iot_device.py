import os


class IoTDevice:
    def __init__(self, serial_number, cloud_id):
        self.serial_number = serial_number
        self.cloud_id = cloud_id

    def __str__(self):
        return f"{self.serial_number}, {self.cloud_id}"


def is_unique(file_path):
    def decorator(func):
        def wrapper(device, *args, **kwargs):
            if os.path.isfile(file_path):
                with open(file_path, 'r') as file:
                    existing_devices = file.read().strip().split('\n')
                    device_str = str(device)
                    if device_str in existing_devices:
                        print(f"Device '{device_str}' already exists in the file.")
                        return
            return func(device, *args, **kwargs)
        return wrapper
    return decorator


@is_unique("device_info.txt")
def write_device_to_file(device, env_var_name):
    file_path = os.getenv(env_var_name)

    if file_path is None:
        raise ValueError(f"Environment variable '{env_var_name}' is not set.")

    with open(file_path, 'a') as file:
        file.write(str(device) + "\n")
    print(f"Device information written to {file_path}")


def read_devices_from_file(env_var_name):
    file_path = os.getenv(env_var_name)

    if file_path is None:
        raise ValueError(f"Environment variable '{env_var_name}' is not set.")

    devices = []

    with open(file_path, 'r') as file:
        for line in file:
            parts = line.strip().split(', ')
            if len(parts) == 2:
                serial_number, cloud_id = parts
                devices.append(IoTDevice(serial_number, cloud_id))

    return devices


