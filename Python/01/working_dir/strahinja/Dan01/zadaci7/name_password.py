import os

if __name__ == '__main__':

    username = os.getenv('USERNAME')
    password = os.getenv('PASSWORD')

    if username is None or password is None:
        print("Environment variables USERNAME and PASSWORD must be set.")
    else:
        filename = f"{username}.txt"

        if os.path.exists(filename):
            with open(filename, 'r') as file:
                current_content = file.read().strip()
            if current_content != password:
                with open(filename, 'w') as file:
                    file.write(password)
                print(f"{filename} updated.")
            else:
                print(f"Password matches.")
        else:
            with open(filename, 'w') as file:
                file.write(password)
            print(f"{filename} je created.")