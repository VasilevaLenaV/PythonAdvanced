# Проверка уровня
import pytest
from task4 import User
from task5 import Project


@pytest.fixture
def project():
    project = Project()
    return project


def test_get_user_level(project):
    project.add_user("User1", 1, 6)
    user = User("User1", 1, 6)

    assert project.get_user_level(user) == 6

