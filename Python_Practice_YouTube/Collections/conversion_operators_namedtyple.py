from collections import namedtuple
import collections

Employee = collections.namedtuple("Employee",["name","age","MobileNo"])

# Adding Values
E = Employee("Cristina",24,7894125630)

# Initializing Iterable
li = ["Kristy",32,4464624648]

# Initializing dictionary
di = {"name" : "Rituja", "age":22, "MobileNo": 5413546456}

print(E._make(li)) # returns a named tuple
print(E._asdict()) # to return ordered dict
print(Employee(**di))