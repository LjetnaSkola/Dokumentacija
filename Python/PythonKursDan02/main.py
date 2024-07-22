from quadratic_equation import solve_quadratic
from fibonacci import fibonacci_generator
from is_palindrome import is_palindrome
from str_cmp import str_cmp
from square import draw_square
from adder import ListAdder, DictAdder
from fraction import Fraction
import os
from iot_device import IoTDevice, write_device_to_file, read_devices_from_file
from user import User, write_users_to_file, read_users_from_file

print("1.Quadratic equation")

a = 1
b = -3
c = 2

solutions = solve_quadratic(a, b, c)

print(f"The solutions are:{solutions}\n")

print("2.Fibonacci generator")

fib_gen = fibonacci_generator()

for _ in range(10):
    print(next(fib_gen))

print()


print("3.Is palindrome?")

input_string = "A man, a plan, a canal, Panama"
result = is_palindrome(input_string)
print("The string is a palindrome." if result else "The string is not a palindrome.")

print()

print("4.strcmp")

str1, str2 = "Apple", "Banana"
result = str_cmp(str1, str2)

if result == 0:
    print("The strings are equal.")
elif result == -1:
    print("String 1 is greater than String 2.")
else:
    print("String 2 is greater than String 1.")

print()


print("5.Square")

draw_square(5)
print()
draw_square(3, '*')

print(f"\n")

print("6.Adder")

list_adder = ListAdder()
result_list = list_adder.add([1, 2, 3], [4, 5, 6])
print("ListAdder Result:", result_list)

dict_adder = DictAdder()
result_dict = dict_adder.add({'a': 1, 'b': 2}, {'c': 3, 'd': 4})
print("DictAdder Result:", result_dict)

print()

print("7.Fraction")

f1 = Fraction(1, 2)
f2 = Fraction(3, 4)

print("Fraction 1:", f1)
print("Fraction 2:", f2)

f3 = f1 + f2
print("Sum:", f3)

f4 = f1 * f2
print("Product:", f4)

print()

print("8.9.10.11.IoTDevice")

device1 = IoTDevice("SN123456", "CLD987654")
device2 = IoTDevice("SN112233", "CLD223455")

os.environ["DEVICE_FILE_PATH"] = "device_info.txt"

with open("device_info.txt", 'w') as file:
    write_device_to_file(device1, "DEVICE_FILE_PATH")
    write_device_to_file(device2, "DEVICE_FILE_PATH")

devices = read_devices_from_file("DEVICE_FILE_PATH")

for device in devices:
    print(device)

print("12.13.User")

os.environ["USER_FILE_PATH"] = "users.txt"
file_path = os.getenv("USER_FILE_PATH")

user1 = User("john@mail.com", "password123", 1)
user2 = User("jane@mail.com", "pass123", 2)

write_users_to_file(file_path, [user1, user2])

users = read_users_from_file(file_path)

for user in users:
    print(user)

print()
