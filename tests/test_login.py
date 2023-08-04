# Проверка входа пользователя
import pytest

from task5 import Project


@pytest.fixture
def project():
    project = Project()
    return project


def test_login(project):
    project.add_user("User1", 1, 8)
    assert project.login("User1", 1) == 8


