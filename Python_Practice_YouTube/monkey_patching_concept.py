# Changing the behavior of code at runtime is called monkey patching

class A:
    def m1(self):
        print("I am m1")

obj1 = A()
obj1.m1()

def m2():
    print("I am m2")

obj1.m1=m2
obj1.m1()