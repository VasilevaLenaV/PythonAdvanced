import json

from task3 import AccessError, LevelError
from task4 import User


# Доработать класс Project
# Доработайте классы исключения так, чтобы они выдали подробную информацию об ошибках.
# Передавайте необходимые данные из основного кода проекта.

def check_access(lvl):
    if lvl < 5:
        raise LevelError("Ошибка уровня")


class Project:
    def __init__(self, users=None):
        self.users = users or set()
        self.admin = None
        self.login_level = 7

    @classmethod
    def fill_users(cls):
        with open("users.json", 'r', encoding="utf-8") as file:
            data = json.load(file)
            file_users = set()
            for user_data in data:
                name = user_data.get('name')
                user_id = user_data.get('user_id')
                access_level = user_data.get('access_level')
                if name and user_id and access_level:
                    file_users.add(User(name, user_id, access_level))
        return cls(file_users)

    def check_user(self, user):
        if user not in self.users:
            raise AccessError("Ошибка доступа",403)

    def login(self, name, user_id):
        try:
            user = (name, user_id)

            self.check_user(user)

        except LevelError as e:
            print(e)
            raise AccessError("Ошибка доступа")

        return self.get_user_level(user)

    def add_user(self, name, user_id, user_level):
        user = (name, user_id)
        if user_level < self.login_level:
            raise LevelError("Ошибка уровня доступа")
        self.users.add(user)

    def get_user_level(self, user):
        return self.login_level

    def __eq__(self, other):
        return isinstance(other, Project) and self.users == other.users
