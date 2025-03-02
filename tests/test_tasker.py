from answer.src.tasker import Task,Task_Manager as tm
import pytest

@pytest.mark.create
def test_create():
    assert tm.create(Task.id,Task.title,Task.description,Task.status,Task.due_date,Task.priority,Task.category)

@pytest.mark.read
def test_read():
    assert tm.read(f"ID: {Task.id}, Title: {Task.title}, Description: {Task.description}, Status: {Task.status}")

@pytest.mark.search
def test_search():
    assert tm.search(f"Title: {Task.title}, Description: {Task.description}, Status: {Task.status}")

@pytest.mark.delete
def test_delete():
    assert tm.delete(Task.id)

@pytest.mark.filter
def test_filter():
    assert tm.filter(Task.status)