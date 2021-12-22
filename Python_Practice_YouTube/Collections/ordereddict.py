scores = [("Rohan",2),("Ankita",5),("Manas",21),("Sita",15)]
d = {}

for name,score in scores:
    d[name]=score

print(d)
print(d.keys())
print(d.values())

from collections import OrderedDict

d_ordered = OrderedDict(scores)
print(d_ordered)
print(d_ordered.keys())
print(d_ordered.values)