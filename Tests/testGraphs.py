import matplotlib.pyplot as plt
import numpy as np

'''
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

str1 = "(25,50,50,32)"
newstr1 = str1.replace("(", "").replace(")","")
sizes1 = list(map(int, newstr1.split(",")))


#sizes = [15, 30, 45, 10]
plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.axis('equal')
#plt.show()


y_pos = np.arange(len(labels))
plt.bar(y_pos, sizes, align='center', alpha=0.5)
plt.xticks(y_pos, labels)
#plt.show()

'''

str2 = "(25,50,50)"
newstr2 = str2.replace("(", "").replace(")","")
sizes = list(map(int, newstr2.split(",")))

print("Generating Grahp")
plt.plot(sizes, sizes)
plt.ylabel("ds ds ds")
plt.xlabel("dsd dsd")
plt.show()
