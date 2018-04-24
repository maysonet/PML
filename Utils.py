import datetime

#Global variables
last_tid = 0
last_uid = 0
p = None

#Util classes
class Task:
    def __init__(self, task, start_date, end_date, status, assigned_to=''):
        self.task = task
        self.start_date = start_date
        self.end_date = end_date
        self.creation_date = datetime.date.today()
        self.status = 0
        global last_tid
        last_tid += 1
        self.id = last_tid

class User:
    def __init__(self, name):
        self.name = name
        global last_uid
        last_uid += 1
        self.id = last_uid

class Project:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.tasks = []
        self.users = []

    def new_task(self, task, start_date, end_date, priority=''):
        self.tasks.append(Task(task, start_date, end_date, priority))

    def new_user(self, name):
        self.users.append(User(name))

    def _find_task(self, task_id):
        for task in self.tasks:
            if str(task.id) == str(task_id):
                return task
        return None

    def edit_task(self, task_id, start_date, end_date):
        task = self._find_task(task_id)
        if task:
            task.start_date = start_date
            task.end_date = end_date
            return True
        return False

    def show_tasks(self, tasks=None):
        if not tasks:
            tasks = self.tasks
        for task in tasks:
            print("{0}: ({1} -- {2})\n{3}".format(
                task.id, task.start_date, task.end_date, task.task))

    def show_users(self, users=None):
        if not users:
            users = self.users
        for user in users:
            print("{0}: {1}".format(user.id, user.name))



#Util methods

def new_project(proj_name, proj_id):
    global p
    p = Project(proj_name, proj_id)
    return 'Project was created: ' + proj_name + ', ' + proj_id

def add_user(user_name):
    global p
    p.new_user(user_name)
    p.show_users()
    return 'User was added: ' + user_name

def edit_user(user_id, user_name):
    pass
def remove_user(user_id):
    pass

def add_task(task, start_date, end_date):
    global p
    p.new_task(task, start_date, end_date)
    p.show_tasks()
    return 'task was added: ' + task + ', ' + start_date + ', ' + end_date

def edit_task(task_id, start_date, end_date):
    pass

def delete_task(task_id):
    pass

def complete_task(task_id): #change task status to 1 (completed)
    pass

def assign_task(task_id, user_id):
    pass

def get_task_status(task_id):
    pass
