from datetime import date
from datetime import datetime
import graphviz as gv #For brainstorming diagram
import functools
import pickle #For data persistense
from plotly.offline import plot
import plotly.figure_factory as ff #For Gantt charts
import matplotlib.pyplot as plt
import numpy as np

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
        self.creation_date = date.today()
        global last_tid
        last_tid += 1
        self.id = last_tid
        self.status = False
        self.assigned_to = None

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
            dff = []
            for t in tasks:
                start = datetime.strptime(t.start_date, '%d-%m-%Y').strftime("%Y-%m-%d")
                end = datetime.strptime(t.end_date, '%d-%m-%Y').strftime("%Y-%m-%d")
                status = 'Complete' if t.status else 'Incomplete'
                entry = dict(Task=t.task, Start=start, Finish=end, Resource=status)
                dff.append(entry)

            print(dff)

            colors = { 'Incomplete': 'rgb(220, 0, 0)',
                      'Complete': 'rgb(0, 255, 100)'}

            fig = ff.create_gantt(dff, colors=colors, index_col='Resource', show_colorbar=True, group_tasks=True)
            plot(fig, filename='gantt/gantt_p' + str(self.id))

        else:
            print("No tasks found in current project.")


    def new_task(self, task, start_date, end_date):
        try:
            start_obj = datetime.strptime(start_date, '%d-%m-%Y')
            end_obj = datetime.strptime(end_date, '%d-%m-%Y')
            self.tasks.append(Task(task, start_date, end_date))
            print("New task added")
        except ValueError:
            print("Date entered is not valid")


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
        try:
            start_obj = datetime.strptime(start_date, '%d-%m-%Y')
            end_obj = datetime.strptime(end_date, '%d-%m-%Y')
            if task is not None:
                task.start_date = start_date
                task.end_date = end_date
                print("Task dates edited.")
            else:
                print("Task with ID:" + str(task_id) + " was not found.")
        except ValueError:
            print("Date entered is not valid")

    def assign_task(self, task_id, member_id):
        task = self._find_task(task_id)
        if task is not None:
            task.assigned_to = member_id
            print("Task assigned to member with ID:" + str(member_id))
        else:
            print("Task with ID:" + str(task_id) + " was not found.")

    def show_tasks(self, tasks=None):
        if not tasks:
            tasks = self.tasks
            print("Showing all tasks... \n")
        for task in tasks:

            print("{0}: {3} [Start Date: {1}, End Date: {2}] [Done?: {4}] [Member id: {5}]\n".format(
                task.id, task.start_date, task.end_date, task.task, task.status, task.assigned_to))

    def show_today(self, tasks=None):
        if not tasks:
            tasks = self.tasks
            today_tasks = []
        for task in tasks:
            end = datetime.strptime(task.end_date, '%d-%m-%Y')
            if end.date() == datetime.today().date():
                today_tasks.append(task)

        if len(today_tasks) > 0:
            print("Showing tasks for today... \n")
            for task in today_tasks:

                print("{0}: {3} [Start Date: {1}, End Date: {2}] [Done?: {4}] [Member id: {5}]\n".format(
                task.id, task.start_date, task.end_date, task.task, task.status, task.assigned_to))
        else:
            print("No tasks are due today.\n")

    def show_week(self, tasks=None):
        if not tasks:
            tasks = self.tasks
            week_tasks = []
            current_week = datetime.today().isocalendar()
        for task in tasks:
            end = datetime.strptime(task.end_date, '%d-%m-%Y').isocalendar()
            if end[0] == current_week[0] and end[1] == current_week[1]:
                week_tasks.append(task)

        if len(week_tasks) > 0:
            print("Showing tasks for this week... \n")
            for task in week_tasks:

                print("{0}: {3} [Start Date: {1}, End Date: {2}] [Done?: {4}] [Member id: {5}]\n".format(
                task.id, task.start_date, task.end_date, task.task, task.status, task.assigned_to))
        else:
            print("No tasks are due for this week.\n")


    def show_overdue(self, tasks=None):
        if not tasks:
            tasks = self.tasks
            overdue_tasks = []
        for task in tasks:
            end = datetime.strptime(task.end_date, '%d-%m-%Y')
            if  datetime.today().date() > end.date() and not task.status:
                overdue_tasks.append(task)

        if len(overdue_tasks) > 0:
            print("Showing overdue tasks... \n")
            for task in overdue_tasks:

                print("{0}: {3} [Start Date: {1}, End Date: {2}] [Done?: {4}] [Member id: {5}]\n".format(
                task.id, task.start_date, task.end_date, task.task, task.status, task.assigned_to))
        else:
            print("No overdue tasks.\n")



    def complete_task(self, task_id):
        task = self._find_task(task_id)
        if task is not None:
            task.status = True
            print("Task with ID:"+ str(task_id) + " marked as completed.")
        else:
            print("Task with ID:" + str(task_id) + " was not found.")
    def generate_project(self, pid):
        file = open(self.name + '.txt', 'w')
        print ('Project text Generated')
        file.close()
        with open(self.name +'.txt', 'w') as f:
            f.write('--------------GENERATE_PROJECT--------------\n\n')
            f.write('Project Name : ' + self.name + '\n\n')
            f.write('Project Id : ' + pid  + '\n\n')
            f.write('Project Members : \n')
            users = None
            if not users:
                users = self.users
            for user in users:
                f.write("{0}: {1}".format(user.id, user.name) + '\n')
            f.write('\nProject Tasks : \n')
            tasks = None
            if not tasks:
                tasks = self.tasks
            for task in tasks:
                f.write("{0}: {3} [Start Date: {1}, End Date: {2}] [Done?: {4}] [Member id: {5}]\n".format(
                    task.id, task.start_date, task.end_date, task.task, task.status, task.assigned_to) + '\n')
            f.close()



    def new_user(self, name):
        self.users.append(User(name))
        print('User was added: ' + str(name))

    def delete_user(self, user_id):
        user = self._find_user(user_id)
        if user is not None:
            print("User with ID:" + str(user_id) + " was found.")
            self.users.remove(user)
            print("User removed...")
        else:
            print("User with ID:" + str(user_id) + " was not found.")

    def delete_task(self, task_id):
        task = self._find_task(task_id)
        if task is not None:
            print("Task with ID:" + str(task_id) + " was found.")
            self.tasks.remove(task)
            print("Task removed...")
        else:
            print("Task with ID:" + str(task_id) + " was not found.")

    def show_users(self, users=None):
        if not users:
            users = self.users
            print("Showing all users... \n")
        for user in users:
            print("{0}: {1}".format(user.id, user.name))


#Util methods

def get_filename(pid):
    global filename
    filename = 'data' + str(pid) + '.PML'
    return filename

def new_project(pname):
    proj = Project(pname)
    print('Project ' + pname + ' was created with ID ' + str(proj.get_pid()))
    save_project(proj)



def save_project(obj):
    file = get_filename(obj.get_pid())
    with open(file, 'wb') as output:
        global last_pid
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
    except FileNotFoundError:
            print("ERROR: No projects created with pid="+str(pid))

def remove_user(uid, pid):
    file = get_filename(pid)

    try:
        #Load project data
        with open(file, 'rb') as input:
            proj = pickle.load(input)
            proj.delete_user(uid)
            global last_uid
            if len(proj.users) > 0:
                last_uid = proj.users[-1].id
            #Add User to project

            save_project(proj)
    except FileNotFoundError:
            print("ERROR: No projects created with pid="+str(pid))

def view_members(pid):
    file = get_filename(pid)
    try:
        #Load project data
        with open(file, 'rb') as input:
            proj = pickle.load(input)
            proj.show_users()
    except FileNotFoundError:
            print("ERROR: No projects created with pid="+str(pid))

def add_task(task, start_date, end_date, pid):
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
    except FileNotFoundError:
            print("ERROR: No projects created with pid="+str(pid))

def remove_task(taskid, pid):
    file = get_filename(pid)
    try:
        #Load project data
        with open(file, 'rb') as input:
            proj = pickle.load(input)
            global last_tid
            if len(proj.tasks) > 0:
                last_tid = proj.tasks[-1].id
            #Remove task from project
            proj.delete_task(taskid)
            save_project(proj)
    except FileNotFoundError:
            print("ERROR: No projects created with pid="+str(pid))

def completed_task(taskid, pid):
    file = get_filename(pid)
    try:
        #Load project data
        with open(file, 'rb') as input:
            proj = pickle.load(input)
            global last_tid
            if len(proj.tasks) > 0:
                last_tid = proj.tasks[-1].id
            #Remove task from project
            proj.complete_task(taskid)
            save_project(proj)
    except FileNotFoundError:
            print("ERROR: No projects created with pid="+str(pid))

def view_tasks(pid):
    file = get_filename(pid)
    try:
        with open(file, 'rb') as input:
            proj = pickle.load(input)
            proj.show_tasks()
    except FileNotFoundError:
            print("ERROR: No projects created with pid="+str(pid))

def view_today(pid):
    file = get_filename(pid)
    try:
        with open(file, 'rb') as input:
            proj = pickle.load(input)
            proj.show_today()
    except FileNotFoundError:
            print("ERROR: No projects created with pid="+str(pid))

def view_week(pid):
    file = get_filename(pid)
    try:
        with open(file, 'rb') as input:
            proj = pickle.load(input)
            proj.show_week()
    except FileNotFoundError:
            print("ERROR: No projects created with pid="+str(pid))

def view_overdue(pid):
    file = get_filename(pid)
    try:
        with open(file, 'rb') as input:
            proj = pickle.load(input)
            proj.show_overdue()
    except FileNotFoundError:
            print("ERROR: No projects created with pid="+str(pid))

def add_idea(idea, pid):
    file = get_filename(pid)
    try:
        #Load project data
        with open(file, 'rb') as input:
            proj = pickle.load(input)
            proj.new_idea(idea)
            save_project(proj)

    except FileNotFoundError:
            print("ERROR: No projects created with pid="+str(pid))

def add_brainstorm(title, pid):
    file = get_filename(pid)
    try:
        #Load project data
        with open(file, 'rb') as input:
            proj = pickle.load(input)
            proj.new_brainstorm(title)
            save_project(proj)

    except FileNotFoundError:
            print("ERROR: No projects created with pid="+str(pid))

def generate_diagram(pid):
    file = get_filename(pid)
    try:
        #Load project data
        with open(file, 'rb') as input:
            proj = pickle.load(input)
            proj.generate_brainstorming_diagram()

    except FileNotFoundError:
            print("ERROR: No projects created with pid="+str(pid))

def generate_gantt(pid):
    file = get_filename(pid)
    try:
        #Load project data
        with open(file, 'rb') as input:
            proj = pickle.load(input)
            proj.generate_gantt_chart()

    except FileNotFoundError:
            print("ERROR: No projects created with pid="+str(pid))

def edit_task(taskid, start_date, end_date, pid):
    file = get_filename(pid)
    try:
        #Load project data
        with open(file, 'rb') as input:
            proj = pickle.load(input)
            global last_tid
            if len(proj.tasks) > 0:
                last_tid = proj.tasks[-1].id
            #Remove task from project
            proj.edit_task(taskid, start_date, end_date)
            save_project(proj)
    except FileNotFoundError:
            print("ERROR: No projects created with pid="+str(pid))

def assign_task(taskid, memberid, pid):
    file = get_filename(pid)
    try:
        #Load project data
        with open(file, 'rb') as input:
            proj = pickle.load(input)
            global last_tid
            if len(proj.tasks) > 0:
                last_tid = proj.tasks[-1].id
            #Remove task from project
            proj.assign_task(taskid, memberid)
            save_project(proj)
    except FileNotFoundError:
            print("ERROR: No projects created with pid="+str(pid))

def generate_project (pid):
    file = get_filename(pid)
    try:
        #Load project data
        with open(file, 'rb') as input:
            proj = pickle.load(input)
            proj.generate_project(pid)
    except FileNotFoundError:
            print("ERROR: No projects created with pid="+str(pid))

# Utils for generating charts
def generate_pie(labels, values):
    cleanstr = labels.replace("(", "").replace(")","")
    labels = cleanstr.split(",")
    cleanint = values.replace("(", "").replace(")","")
    values = list(map(int, cleanint.split(",")))

    if len(labels) != len(values):
        print("ERROR: # of Labels must match # of Values")
    else:
        print("Generating pie chart...")
        plt.pie(values, labels=labels, autopct='%1.1f%%')
        plt.axis('equal')
        plt.show()

def generate_bar(labels, values):
    cleanstr = labels.replace("(", "").replace(")","")
    labels = cleanstr.split(",")
    cleanint = values.replace("(", "").replace(")","")
    values = list(map(int, cleanint.split(",")))

    if len(labels) != len(values):
        print("ERROR: # of Labels must match # of Values")
    else:
        print("Generating bar chart...")
        y_pos = np.arange(len(labels))
        plt.bar(y_pos, values, align='center', alpha=0.5)
        plt.xticks(y_pos, labels)
        plt.show()

'''
#Generic Code to LOAD existing project
filename = "data.PML"
with open(filename, 'rb') as input:
    loaded_data = pickle.load(input)
'''
