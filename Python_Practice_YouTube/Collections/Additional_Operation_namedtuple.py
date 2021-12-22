import collections

Employee = collections.namedtuple("Employee",["name","age","MobileNo"])

E = Employee("Cristina",24,7894125630)

print((E._fields))
print(E._replace(name="Shrishty"))