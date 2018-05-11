from datetime import date
from datetime import datetime
import graphviz as gv #For brainstorming diagram
import functools
import pickle #For data persistense
import gantt #For Gantt charts
from dateutil import rrule

#Global variables
last_tid = 0
last_uid = 0
last_pid = 0
filename = None

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

#Utils for Gantt charts
#gantt.define_font_attributes(fill='black',
#                             stroke='black',
#                             stroke_width=0,
#                             font_family="Verdana")
def weeks_between(start_date, end_date):
    weeks = rrule.rrule(rrule.WEEKLY, dtstart=start_date, until=end_date)
    return weeks.count()

#Util classes
class Brainstorm:
    def __init__(self, title):
        self.ideas = []
        self.title = title

class Task:
    def __init__(self, task, start_date, end_date, status, assigned_to=''):
        self.task = task
        self.start_date = start_date
        self.end_date = end_date
        self.creation_date = date.today()
        global last_tid
        last_tid += 1
        self.id = last_tid
        self.status = status

class User:
    def __init__(self, name):
        self.name = name
        global last_uid
        last_uid += 1
        self.id = last_uid

class Project:
    def __init__(self, name):
        self.name = name
        global last_pid
        last_pid += 1
        self.id = last_pid
        self.tasks = []
        self.users = []
        self.bs = None
        self.total_users = 0
        self.total_tasks = 0


    def get_pid(self):
        return self.id

    def new_brainstorm(self, title):
        self.bs = Brainstorm(title)
        print("Brainstorming was created.")

    def new_idea(self, idea):
        brainstorm = self.bs
        if brainstorm is not None:
            brainstorm.ideas.append(idea)
            print(brainstorm.ideas[len(brainstorm.ideas)-1] + " added successfully to " + brainstorm.title)
        else:
            print("Brainstorming not found for this project")

    def generate_brainstorming_diagram(self):
        brainstorm = self.bs
        if brainstorm is not None:
            print("Generating diagram...")
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

    def generate_gantt_chart(self):
        tasks = self.tasks
        if tasks is not None:
            print("Generating diagram for " + self.name)
            proj = gantt.Project(name=self.name)

            for t in tasks:
                print(t.task)
                print(t.start_date)
                print(t.end_date)


                start_obj = datetime.strptime(t.start_date, '%d-%m-%Y')
                end_obj = datetime.strptime(t.end_date, '%d-%m-%Y')
                duration = weeks_between(start_obj, end_obj)
                print(duration)

                t = gantt.Task(name=t.task,start=start_obj,duration=duration)
                proj.add_task(t)

            proj.make_svg_for_tasks(filename='gantt/gantt_p' + str(self.id) + '.svg')

        else:
            print("No tasks found in current project.")


    def new_task(self, task, start_date, end_date):
        #Validate dates

        try:
            start_obj = datetime.strptime(start_date, '%d-%m-%Y')
            end_obj = datetime.strptime(end_date, '%d-%m-%Y')
            status = 0
            self.tasks.append(Task(task, start_date, end_date, status))
            self.total_tasks += 1
            print('Task was added: ' + task + ', ' + start_date + ', ' + end_date + ', ' + status)

        except ValueError:
            print("date not valid")


    def _find_task(self, task_id):
        for task in self.tasks:
            if str(task.id) == str(task_id):
                return task
        return None

    def _find_user(self, user_id):
        for user in self.users:
            if str(user.id) == str(user_id):
                return user
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

    def complete_task(self, task_id): #change task status to 1 (completed)
        #pass
        task = self._find_task(task_id)
        if task:
            task.status = 1
            return True
        return False

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
    def delete_user(self, user_id):
        #pass
        user = self._find_user(user_id)
        if user is not None:
            print("User with ID:" + str(user_id) + " was found.")
            self.users.remove(user)
            self.total_users -= 1
            print("User removed...")

        else:
            print("User with ID:" + str(user_id) + " was not found.")

    def delete_task(self, task_id):
        # En proceso !!!!!!
        #pass
        task = self._find_task(task_id)
        if task is not None:
            print("Task with ID:" + str(task_id) + " was found.")
            self.tasks.remove(task)
            self.total_tasks -= 1
            print("Task removed...")
        else:
            print("Task with ID:" + str(task_id) + " was not found.")

    def show_users(self, users=None):
        if not users:
            users = self.users
        for user in users:
            print("{0}: {1}".format(user.id, user.name))

#Util methods

def get_filename(pid):
    global filename
    filename = 'data' + str(pid) + '.PML'
    return filename

def new_project(pname):
    proj = Project(pname)
    print('Project Created with ID:' + str(proj.get_pid()))
    save_project(proj)


def save_project(obj):
    file = get_filename(obj.get_pid())
    with open(file, 'wb') as output:
        pickle.dump(obj, output, pickle.HIGHEST_PROTOCOL)

def add_user(username, pid):
    file = get_filename(pid)
    try:
        #Load project data
        with open(file, 'rb') as input:
            proj = pickle.load(input)
            global last_uid
            if len(proj.users) > 0:
                last_uid = proj.users[-1].id
            #Add User to project
            proj.new_user(username)
            save_project(proj)
            proj.show_users()
    except FileNotFoundError:
            print("ERROR: No projects created")

def remove_user(uid, pid):
    file = get_filename(pid)

    try:
        #Load project data
        with open(file, 'rb') as input:
            proj = pickle.load(input)
            global last_uid
            last_uid = proj.total_users
            #Add User to project
            proj.delete_user(uid)
            save_project(proj)
            proj.show_users()
    except FileNotFoundError:
            print("ERROR: No projects created")

def view_members(pid):
    file = get_filename(pid)
    try:
        #Load project data
        with open(file, 'rb') as input:
            proj = pickle.load(input)
            proj.show_users()
    except FileNotFoundError:
            print("ERROR: No projects created")

def add_task(task, start_date, end_date, pid):
    print('pid : ', pid)
    file = get_filename(pid)
    try:
        #Load project data
        with open(file, 'rb') as input:
            proj = pickle.load(input)
            global last_tid
            if len(proj.tasks) > 0:
                last_tid = proj.tasks[-1].id
            #Add Task to project
            proj.new_task(task, start_date, end_date)
            save_project(proj)
            #proj.show_tasks()
    except FileNotFoundError:
            print("ERROR: No projects created")

def remove_task(taskid, pid):
    file = get_filename(pid)
    try:
        #Load project data
        with open(file, 'rb') as input:
            proj = pickle.load(input)
            global last_taskid
            last_taskid = proj.total_tasks
            #Remove task from project
            proj.delete_task(taskid)
            save_project(proj)
            proj.show_tasks()
    except FileNotFoundError:
            print("ERROR: No projects created")

def completed_task(taskid, pid):
    file = get_filename(pid)
    try:
        #Load project data
        with open(file, 'rb') as input:
            proj = pickle.load(input)
            global last_taskid
            last_taskid = proj.total_tasks
            #Remove task from project
            proj.complete_task(taskid)
            save_project(proj)
            proj.show_tasks()
    except FileNotFoundError:
            print("ERROR: No projects created")

def view_tasks(pid):
    file = get_filename(pid)
    try:
        #Load project data
        with open(file, 'rb') as input:
            proj = pickle.load(input)
            proj.show_tasks()
    except FileNotFoundError:
            print("ERROR: No projects created")

def add_idea(idea, pid):
    file = get_filename(pid)
    try:
        #Load project data
        with open(file, 'rb') as input:
            proj = pickle.load(input)
            proj.new_idea(idea)
            save_project(proj)

    except FileNotFoundError:
            print("ERROR: No projects created")

def add_brainstorm(title, pid):
    file = get_filename(pid)
    try:
        #Load project data
        with open(file, 'rb') as input:
            proj = pickle.load(input)
            proj.new_brainstorm(title)
            save_project(proj)

    except FileNotFoundError:
            print("ERROR: No projects created")

def generate_diagram(pid):
    file = get_filename(pid)
    try:
        #Load project data
        with open(file, 'rb') as input:
            proj = pickle.load(input)
            proj.generate_brainstorming_diagram()
            #save_project(proj)

    except FileNotFoundError:
            print("ERROR: No projects created")



'''
#Generic Code to LOAD existing project
filename = "data.PML"
with open(filename, 'rb') as input:
    loaded_data = pickle.load(input)
'''
