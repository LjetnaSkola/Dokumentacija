import os
import bcrypt

class IotDev:
    """
    Represents an IOT Device
    """

    def __init__(self, serial_num: int, cloud_id: int):
        """
        Args:
            serial_num: serial number
            cloud_id: Id on the cloud
        """
        self.cloud_id = cloud_id
        self.serial_num = serial_num

    def __str__(self):
        return str(self.serial_num) + ", " + str(self.cloud_id)
    
    def write_to_file(self):
        file_name = os.environ.get("FILE_NAME")
        with open(file_name, "a") as f:
            f.write(str(self))
            f.write("\n")

    @staticmethod
    def read_from_file() -> list[None]:
        file_name = os.environ.get("FILE_NAME")
        list_ = []
        
        if not os.path.exists(file_name):
            print("File does not exist")
            return None
        
        with open(file_name, "r") as f:
            for line in f:
                parts = line.replace(" ", "").split(",")
                list_.append(IotDev(int(parts[0]), int(parts[1])))

        return list_


def is_unique(func):
    def wrapper(device: IotDev):
        devs = IotDev.read_from_file()
        if devs is not None:
            ser_nums = [k.serial_num for k in devs]
            if device.serial_num in ser_nums:
                print(f"Serial number: {device.serial_num} already exists!")
                return False
        func(device)
        print(f"Successfully added: {device.serial_num}")
        return True
    return wrapper


IotDev.write_to_file = is_unique(IotDev.write_to_file)


def check_passw(func):
    def wrapper(*args):
        users = User.read_from_file()
        user = [(u.passw, u.email, u.role) for u in users if u.email == args[0]]
        if len(user) > 0:
            if bcrypt.checkpw(args[1].encode('utf-8'), user[0][0].encode('utf-8')):
                print("Valid password!")
                return func(user[0][1], user[0][0], user[0][2])
            else:
                raise Exception("Invalid password!")
        else:
            raise Exception("User not found")
    return wrapper


def check_email(func)


class User:
    def __init__(self, email: str, passw: str, role: int):
        self.email = email
        self.passw = passw
        self.role = role

    def __str__(self):
        return self.email + "," + self.hash_password() + "," + str(self.role)


    def write_to_file(self):
        file_name = os.environ.get("USER_FILE")
        with open(file_name, "a") as f:
            f.write(str(self))
            f.write("\n")
        
    def hash_password(self):
        salt = bcrypt.gensalt()
        hashed_passw = bcrypt.hashpw(self.passw.encode('utf-8'), salt)
        return hashed_passw.decode('utf-8')


    @check_passw
    @staticmethod
    def login(email, passw, role):
        return User(email, passw, role)
    
    @staticmethod
    def read_from_file():
        file_name = os.environ.get("USER_FILE")
        list_ = []
        
        if not os.path.exists(file_name):
            print("File does not exist")
            return None
        
        with open(file_name, "r") as f:
            for line in f:
                parts = line.split(",")
                list_.append(User(parts[0], parts[1], parts[2]))

        return list_



# User.login = check_passw(User.login)


def main():
    dev1 = IotDev(0,1)
    dev2 = IotDev(2,1)
    dev3 = IotDev(1,2)
    os.environ["FILE_NAME"] = "test.txt"
    os.environ["USER_FILE"] = "users.txt"
    IotDev.write_to_file(dev1)
    IotDev.write_to_file(dev2)
    IotDev.write_to_file(dev3)

    user = User("mail@mail.com", "password", 1)
    user.write_to_file()
    User.login("mail@mal.com", "password")

if __name__ == "__main__":
    main()
