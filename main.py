
from task3 import AccessError, LevelError
from task5 import Project

prj = Project()
prj.fill_users()

# Вход пользователя в систему
try:
    user_level = prj.login("Ivanov", 5)
    print(f"User level: {user_level}")
except AccessError as e:
    print(e)

# Добавление пользователя
try:
    prj.add_user("Denisov", 123, 2)
except LevelError as e:
    print(e)
