import json

from task3 import AccessError, LevelError, IOUserError
from task4 import User, Role


# Доработать класс Project
# Доработайте классы исключения так, чтобы они выдали подробную информацию об ошибках.
# Передавайте необходимые данные из основного кода проекта.

def check_access(lvl):
    if lvl < 5:
        raise LevelError("Ошибка уровня")


class Project:
    def __init__(self, users=None, roles=None):
        self.users = users or set()
        self.roles = roles or set()
        self.admin = None
        self.login_level = 7

    @classmethod
    def fill_users(cls):
        with open("users.json", 'r', encoding="utf-8") as file:
            data = json.load(file)
            file_users = set()
            role_users = set()
            for user_data in data:
                name = user_data.get('name')
                user_id = user_data.get('user_id')
                access_level = user_data.get('access_level')
                user_role = user_data.get("roles")
                user = User(name, user_id, access_level)
                role_ = Role(user_id, user_role)

                if name and user_id and access_level:
                    file_users.add(user)
                if user_role:
                    role_users.add(role_)

        return cls(file_users, role_users)

    def check_user(self, user):
        for u in list(self.users):
            if not (user[0] == u[0] and user[1] == u[1]):
                raise AccessError("Ошибка доступа", 403)

    def check_role(self, userid, role):
        return True

    def login(self, name, user_id):
        try:
            user = (name, user_id)

            self.check_user(user)

        except LevelError as e:
            print(e)
            raise AccessError("Ошибка доступа")

        return self.get_user_level(user)

    def logout(self):
        pass

    def update_user(self, user):
        pass

    def add_user(self, name, user_id, user_level):
        user = (name, user_id, user_level)
        if user_level < self.login_level:
            raise LevelError("Ошибка уровня доступа")
        if user in self.users:
            raise IOUserError("Пользователь с данным именем уже существует")

        self.users.add(user)

    def get_user_level(self, user):
        for u in list(self.users):
            if u[0] == user[0]:
                return u[2]

        return self.login_level

    def __eq__(self, other):
        return isinstance(other, Project) and self.users == other.users
