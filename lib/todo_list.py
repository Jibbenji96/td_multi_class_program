class TodoList:
    def __init__(self):
        self.task_list = []


    def add(self, todo):
        if not todo:
            raise Exception("No todo task to add")
        self.task_list.append(todo)


    def incomplete(self):
        incomplete_tasks = []
        for entry in self.task_list:
            if entry.complete == False:
                incomplete_tasks.append(entry)
        return incomplete_tasks


    def complete(self):
        complete_tasks = []
        for entry in self.task_list:
            if entry.complete == True:
                complete_tasks.append(entry)
        return complete_tasks


    def give_up(self):
        for entry in self.task_list:
            if entry.complete == False:
                entry.complete = True
        

