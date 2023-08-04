import pytest
from task5 import Project


@pytest.fixture
def project():
    project = Project()
    return project
