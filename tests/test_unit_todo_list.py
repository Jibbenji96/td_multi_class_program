from lib.todo_list import TodoList
import pytest


def test_todo_list_instantiates():
    todo_list = TodoList()
    assert type(todo_list) == TodoList


def test_todo_list_returns_empty_list_after_instantiation():
    todo_list = TodoList()
    assert todo_list.task_list == []


def test_todo_list_add_none_raises_exception():
    todo_list = TodoList()
    with pytest.raises(Exception) as e:
        todo_list.add(None)
    assert str(e.value) == "No todo task to add"


def test_todo_list_add_empty_string_raises_exception():
    todo_list = TodoList()
    with pytest.raises(Exception) as e:
        todo_list.add("")
    assert str(e.value) == "No todo task to add"