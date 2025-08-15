from lib.todo_list import TodoList

def test_todo_list_instantiates():
    todo_list = TodoList()
    assert type(todo_list) == TodoList

def test_todo_list_returns_empty_list_after_instantiation():
    todo_list = TodoList()
    assert todo_list.task_list == []

