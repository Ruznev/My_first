class Task:
    def __init__(self, title, description, status="Не выполнено", due_date=None, priority="Средний", category="Работа"):
        self.id = None
        self.title = title
        self.description = description
        self.status = status
        self.due_date = due_date  
        self.priority = priority  
        self.category = category

    def to_dict(self):
        return {
        "id": self.id,
        "title": self.title,
        "description": self.description,
        "status": self.status
        }
        
class Task_Manager:

    def __init__(self):
        self.tasks = [] 

    def create(self, task):
        task.id = len(self.tasks) + 1
        self.tasks.append(task)

    def read(self):
        return self.tasks

    def update(self, task_id, new_status):
        for task in self.tasks:
            if task.id == task_id:
                task.status = new_status
                return True
        return False

    def delete(self, task_id):
        self.tasks = [task for task in self.tasks if task.id != task_id]
        return True

    def search(self, keyword):
        return [task for task in self.tasks if keyword.lower() in task.title.lower() or keyword.lower() in task.description.lower()]

    def filter(self, status):
        return [task for task in self.tasks if task.status == status]

def aboba():
    pass