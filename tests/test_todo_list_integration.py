from lib.todo_list import TodoList
from lib.todo import ToDo
import pytest

def test_todo_list_returns_incomplete_task_instances():
    todo_list = TodoList()
    todo_list.task_list # => []
    todo1 = ToDo("First task")
    todo2 = ToDo("Second task")
    todo2.mark_complete()
    todo_list.add(todo1) # returns nothing, adds todo instance to task_list
    todo_list.add(todo2) # returns nothing, adds second todo instance
    # assert todo_list.incomplete() == [todo1]
    # assert todo_list.complete() == [todo2]
    pass

def test_todo_list_adds_todo_instance_to_list():
    todo_list = TodoList()
    todo1 = ToDo("First task")
    todo_list.add(todo1)
    assert todo_list.task_list == [todo1]


def test_todo_list_returns_incomplete_todo_instances():
    todo_list = TodoList()
    todo1 = ToDo("First task")
    todo_list.add(todo1)
    assert todo_list.incomplete() == [todo1]

def test_todo_list_returns_complete_todo_instances():
    todo_list = TodoList()
    todo1 = ToDo("First task")
    todo2 = ToDo("Second task")
    todo1.mark_complete()
    todo_list.add(todo1)
    todo_list.add(todo2)
    assert todo_list.complete() == [todo1]

def test_todo_list_returns_complete_todo_instances_if_instance_complete_after_adding_to_todo_list():
    todo_list = TodoList()
    todo1 = ToDo("First task")
    todo_list.add(todo1)
    todo1.mark_complete()
    assert todo_list.complete() == [todo1]

def test_todo_list_changes_complete_attribute_of_todo_tasks_to_true_to_give_up():
    todo_list = TodoList()
    todo1 = ToDo("First task")
    todo2 = ToDo("Second task")
    todo_list.add(todo1)
    todo_list.add(todo2)
    todo_list.give_up()
    assert todo_list.incomplete() == []




