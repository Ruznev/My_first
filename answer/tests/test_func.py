from answer.src.tasker import Task,Task_Manager
import pytest

@pytest.mark.calc
def test_create():
    assert Task_Manager().create('Сделать домашнюю работу', 'Написать отчет по математике')

@pytest.mark.calc
def test_read():
    assert Task_Manager().read(f"ID: {Task().task.id}, Title: {Task().task.title}, Description: {Task().task.description}, Status: {Task().task.status}")

@pytest.mark.calc
def test_search():
    assert Task_Manager().search()

@pytest.mark.calc
def test_delete():
    assert Task_Manager().delete()

@pytest.mark.calc
def test_filter():
    assert Task_Manager().filter('не выполнено')