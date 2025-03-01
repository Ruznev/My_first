from src.tasker import Task,Task_Manager as tm
import pytest

@pytest.mark.calc
def test_create():
    assert tm.create(Task.title, Task.description)

@pytest.mark.calc
def test_read():
    assert tm.read(f"ID: {Task.id}, Title: {Task.title}, Description: {Task.description}, Status: {Task.status}")

@pytest.mark.calc
def test_search():
    assert tm.search(f"Title: {Task.title}, Description: {Task.description}, Status: {Task.status}")

@pytest.mark.calc
def test_delete():
    assert tm.delete(int(Task.id))

@pytest.mark.calc
def test_filter():
    assert tm.filter(filter(Task.status))