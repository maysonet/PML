
import Utils
from datetime import date
from datetime import datetime
from plotly.offline import plot
import plotly.figure_factory as ff



p1 = Utils.Project("Test project")
print(p1.get_pid())


#Date Format: DD-MM-YYYY   **MUST VALIDATE IN INPUT

p1.new_task("a new task", "21-07-2019", "25-12-2019")
p1.new_task("testing", "31-12-2018", "29-06-2019")

tasks = p1.tasks


dff = []
for t in tasks:
    start = datetime.strptime(t.start_date, '%d-%m-%Y').strftime("%Y-%m-%d")
    end = datetime.strptime(t.end_date, '%d-%m-%Y').strftime("%Y-%m-%d")
    status = 'Complete' if t.status else 'Incomplete'
    entry = dict(Task=t.task, Start=start, Finish=end, Resource=status)
    dff.append(entry)

print(dff)

df = [dict(Task="Job A", Start='2009-01-01', Finish='2009-02-28', Resource='Complete'),
      dict(Task="Job B", Start='2009-03-05', Finish='2009-04-15', Resource='Not Started'),
      dict(Task="Job C", Start='2009-02-20', Finish='2009-05-30', Resource='Incomplete')]

print(df)



colors = {'Not Started': 'rgb(220, 0, 0)',
          'Incomplete': (1, 0.9, 0.16),
          'Complete': 'rgb(0, 255, 100)'}

#fig = ff.create_gantt(df, colors=colors, index_col='Resource', show_colorbar=True, group_tasks=True)
#plot(fig, filename='gantt-simple-gantt-chart', image='png')
