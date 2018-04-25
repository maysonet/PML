import datetime
import graphviz as gv
import functools
import pickle

#Global variables
last_tid = 0
last_uid = 0
filename = "data.PML"

#Utils for generating diagrams
graph = functools.partial(gv.Graph, format='png')
digraph = functools.partial(gv.Digraph, format='png')
def add_nodes(graph, nodes):
    for n in nodes:
        if isinstance(n, tuple):
            graph.node(n[0], **n[1])
        else:
            graph.node(n)
    return graph

def add_edges(graph, edges):
    for e in edges:
        if isinstance(e[0], tuple):
            graph.edge(*e[0], **e[1])
        else:
            graph.edge(*e)
    return graph

#Util classes
class Brainstorm:
    def __init__(self, title):
        self.ideas = []
        self.title = title

class Task:
    def __init__(self, task, start_date, end_date, status='', assigned_to=''):
        self.task = task
        self.start_date = start_date
        self.end_date = end_date
        self.creation_date = datetime.date.today()
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
        self.bs = None
        self.total_users = 0
        self.total_tasks = 0


    def new_brainstorm(self, title):
        self.bs = Brainstorm(title)

    def add_idea(self, idea):
        brainstorm = self.bs
        if brainstorm is not None:
            brainstorm.ideas.append(idea)
            print(brainstorm.ideas[len(brainstorm.ideas)-1] + " added successfully to " + brainstorm.title)
        else:
            print("Brainstorming not found for this project")

    def generate_brainstorming_diagram(self):
        brainstorm = self.bs
        if brainstorm is not None:
            #print(brainstorm.title)
            #print(brainstorm.ideas)
            arr1 = []
            arr2 = []
            arr1.append(brainstorm.title)
            for i in range(len(brainstorm.ideas)):
                arr1.append(brainstorm.ideas[i])
                tup = (brainstorm.title, brainstorm.ideas[i])
                arr2.append(tup)
            g = add_edges(
                    add_nodes(digraph(), arr1),
                    arr2
                )
            g.render('diagrams/brainstorm', view=True)

    def new_task(self, task, start_date, end_date):
        self.tasks.append(Task(task, start_date, end_date))
        self.total_tasks += 1
        print('Task was added: ' + task + ', ' + start_date + ', ' + end_date)

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

    def delete_task(task_id):
        pass

    def complete_task(task_id): #change task status to 1 (completed)
        pass

    def assign_task(task_id, user_id):
        pass

    def get_task_status(task_id):
        pass

    def new_user(self, name):
        self.users.append(User(name))
        self.total_users += 1
        print('User was added: ' + name)

    def edit_user(user_id, user_name):
        pass
    def remove_user(user_id):
        pass

    def show_users(self, users=None):
        if not users:
            users = self.users
        for user in users:
            print("{0}: {1}".format(user.id, user.name))

#Util methods

def new_project(pname, pid):
    save_project(Project(pname, pid))
    print('Project created.')

def save_project(obj):
    with open(filename, 'wb') as output:
        pickle.dump(obj, output, pickle.HIGHEST_PROTOCOL)

def add_user(username):
    try:
        #Load project data
        with open(filename, 'rb') as input:
            proj = pickle.load(input)
            global last_uid
            last_uid = proj.total_users
            #Add User to project
            proj.new_user(username)
            save_project(proj)
            proj.show_users()
    except FileNotFoundError:
            print("ERROR: No projects created")

def add_task(task, start_date, end_date):
    try:
        #Load project data
        with open(filename, 'rb') as input:
            proj = pickle.load(input)
            global last_tid
            last_tid = proj.total_tasks
            #Add Task to project
            proj.new_task(task, start_date, end_date)
            save_project(proj)
            proj.show_tasks()
    except FileNotFoundError:
            print("ERROR: No projects created")



'''
#Generic Code to LOAD existing project
filename = "data.PML"
with open(filename, 'rb') as input:
    loaded_data = pickle.load(input)
'''
