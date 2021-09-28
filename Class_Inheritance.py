class Bird:

    def __init__(self):
        self.num_eyes=2

    def fly(self):
        print("Flying in Air")
        
class Sparrow(Bird): 

    def __init__(self):
        super().__init__()  # This will inherit everything from class Bird, attributes & methods

    def fly(self):
        super().fly()   # In case you want to add something on the top of method of parent class
        print("I am very small bird.")

    def breathe(self):  # Extra methods can also be added in the Child class.
        print("I can breathe.")

chimpu=Sparrow()
chimpu.fly()
chimpu.breathe()