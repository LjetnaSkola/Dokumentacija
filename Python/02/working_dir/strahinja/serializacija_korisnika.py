import os
from korisnik import Korisnik


def read_from_file():
    path_ = os.getenv("OUT_USERS")
    if not path_:
        print("Environment variable OUT_USERS not set.")
    with open(path_, "r") as file_:
        users = file_.read().split("(")

    iot_users = [
        Korisnik(email.strip(), hash.strip(), role.strip(), True)
        for user in users
        if user.strip()
        for email, hash, role in [user.rsplit(")", 1)[0].split(",")]
    ]

    return iot_users


def write_to_file(user):
    def __write(userIn):
        path_ = os.getenv("OUT_USERS")
        if not path_:
            print("Environment variable OUT_USERS not set.")
        with open(path_, "a") as file_:
            file_.write(str(userIn))

    __write(user)


if __name__ == "__main__":
    write_to_file(Korisnik("johndoe", "sigurnost", 2))
    for i in read_from_file():
        print(i)
