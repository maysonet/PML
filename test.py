import Utils
import pickle


global p
p = Utils.Project("Test project")
print(p.get_pid())
p = Utils.Project("Test project2")
print(p.get_pid())

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
p.new_brainstorm("main topic")
p.add_idea("idea 1")
p.add_idea("idea 2")
p.add_idea("idea 3")
p.add_idea("idea 4")
p.add_idea("idea 5")

p.generate_brainstorming_diagram()
'''
