# Проверка добавление пользователя

import pytest

from task3 import LevelError, AccessError, IOUserError
from task4 import User
from task5 import Project


@pytest.fixture
def project():
    project = Project()
    return project


def test_err_level(project):
    with pytest.raises(LevelError):
        project.add_user("User1", 1, 5)


def test_err_iouser(project):
    project.add_user("User2", 5, 10)
    with pytest.raises(IOUserError):
        project.add_user("User2", 5, 10)
