import Utils
import pickle


global p
p = Utils.Project("Test project")
print(p.get_pid())
p = Utils.Project("Test project2")
print(p.get_pid())
'''
p.new_brainstorm("main topic")
p.add_idea("idea 1")
p.add_idea("idea 2")
p.add_idea("idea 3")
p.add_idea("idea 4")
p.add_idea("idea 5")

p.generate_brainstorming_diagram()
'''
