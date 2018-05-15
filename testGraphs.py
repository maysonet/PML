import matplotlib.pyplot as plt
import numpy as np
str = "(Car, bike, train)"
newstr = str.replace("(", "").replace(")","")
print(newstr)

#print(string.split(","))
#labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
#print(labels)
labels = newstr.split(",")
print(labels)

str2 = "(25,50,50)"
newstr2 = str2.replace("(", "").replace(")","")
sizes = list(map(int, newstr2.split(",")))
#sizes = [15, 30, 45, 10]
plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.axis('equal')
plt.show()


y_pos = np.arange(len(labels))
plt.bar(y_pos, sizes, align='center', alpha=0.5)
plt.xticks(y_pos, labels)
plt.show()

'''
def new_LineGraph(self, name):
    self.pG = Pie(name)
    print("Line Graph was created.")

def generate_lineplot(ylabel, xlabel, ydata, xdata):
    print("Generating Grahp")
    plt.plot(xdata, ydata)
    plt.ylabel(ylabel)
    plt.xlabel(xlabel)
    plt.show()

def new_barGraph(self, name):
    self.pG = Pie(name)
    print("Bar Graph was created.")

def generate_barplot(names, values):
    print("Generating Grahp")
    objects = names
    y_pos = np.arange(len(objects))
    plt.bar(y_pos, values, align='center', alpha=0.5)
    plt.xticks(y_pos, objects)
    plt.show()

'''
