import Utils
import pickle
from datetime import datetime

global p
p0 = Utils.Project("Test project")
print(p0.get_pid())
#p1 = Utils.Project("Test project2")
#print(p1.get_pid())


#Date Format: DD-MM-YYYY   **MUST VALIDATE IN INPUT

p0.new_task("a new task", "21-07-2017", "14-06-2018")
p0.new_task("testing", "31-12-2018", "29-06-2019")
p0.new_task("testing", "31-12-2018", "30-06-2019")
p0.new_task("testing", "31-12-2018", "29-04-2019")

p0.show_today();


#p1.new_task("task1", "21-07-2018", "25-08-2018")
#p1.new_task("task2", "27-39-2018", "29-09-2018")


#p0.generate_gantt_chart()
#p1.generate_gantt_chart()

#datetime_object = datetime.strptime('21-07-1994', '%d-%m-%Y')
#print(datetime_object)

'''
p.new_user("chris")
p.new_user("che")
p.new_user("gre")
p.new_user("frankie")
p.new_user("millie")

p.show_users()



p.delete_user(30)
p.show_users()
p.new_user("greds")
p.show_users()
p.delete_user(5)
p.show_users()
'''
'''
p.new_brainstorm("main topic")
p.add_idea("idea 1")
p.add_idea("idea 2")
p.add_idea("idea 3")
p.add_idea("idea 4")
p.add_idea("idea 5")

p.generate_brainstorming_diagram()
'''
