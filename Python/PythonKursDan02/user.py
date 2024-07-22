import hashlib
import os


class User:
    def __init__(self, email, password, role):
        self.email = email
        self.password = self.encode_password(password)
        self.role = role

    @staticmethod
    def encode_password(password):
        return hashlib.sha256(password.encode()).hexdigest()

    def __str__(self):
        return f"{self.email},{self.password},{self.role}"


def write_users_to_file(file_path, users):
    with open(file_path, 'w') as file:
        for user in users:
            file.write(f"{user}\n")


def read_users_from_file(file_path):
    users = []
    with open(file_path, 'r') as file:
        for line in file:
            email, password, role = line.strip().split(',')
            users.append(User(email, password, int(role)))
    return users
