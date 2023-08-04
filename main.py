# На семинаре 13 был создан проект по работе с пользователями (имя, id, уровень).
# Напишите 3-7 тестов pytest для данного проекта.
# Используйте фикстуры.
import pytest

from task3 import AccessError, LevelError, IOUserError
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
    prj.add_user("Denisov", 10, 100)
except LevelError as e:
    print(e)
except IOUserError as u:
    print(u)


if __name__ == "__main__":
    pytest.main()

