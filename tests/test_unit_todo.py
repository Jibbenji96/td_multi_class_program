from lib.todo import ToDo
import pytest

def test_todo_instantiates():
    todo = ToDo("Walk the dog")
    assert type(todo) == ToDo

def test_todo_assigns_task():
    todo = ToDo("Walk the dog")
    assert todo.task == "Walk the dog"

def test_todo_changes_complete_property_to_true():
    todo = ToDo("Walk the dog")
    todo.mark_complete()
    assert todo.complete == True
