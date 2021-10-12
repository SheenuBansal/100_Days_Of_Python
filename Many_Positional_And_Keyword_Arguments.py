# *args - Many positional arguments
# Type of args is Tuple

# Calcualting sum of multiple numbers.
def add(*args):
    sum = 0
    for n in args:
        sum+=n
    print(sum)
    print(type(args))
add(4,8,9,5,47,2,63,45)

# **kwargs - Many Keyword Arguments
# Type of args is Dictionary

def calculate(**kwargs):
    # print(kwargs)
    # print(type(kwargs))
    for key,value in kwargs.items():
        print(key)
        print(value)

calculate(add=5,multiply=8)

# ---------------------------------------

def calculate(n,**kwargs):
    # print(kwargs)
    n+=kwargs["add"]
    n*=kwargs["multiply"]
    print(n)

calculate(4,add=5,multiply=8)

# ----------------------------------------

class Car :
    def __init__(self,**kwargs):
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")
        self.color = kwargs.get("color")
        self.price = kwargs.get("price")

car_object=Car(make="Maruti")
print(car_object.make)
print(car_object.model)