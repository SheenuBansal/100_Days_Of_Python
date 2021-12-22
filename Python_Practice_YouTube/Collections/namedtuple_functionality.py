from collections import namedtuple
import collections

Student = collections.namedtuple('Student',['name','age','DOB'])

S = Student("Manu",45,'23081990')
print(S[0]) # Access using index
print(S.age) # Access using name
print(getattr(S,"name")) # Access using getattr - i.e. getattribute

