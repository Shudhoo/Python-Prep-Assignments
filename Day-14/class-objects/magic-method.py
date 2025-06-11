# This is an example of class-object using the magic method called "__init__"

class Dog:
    def __init__(self, name):
        self.name = name
    def talk(self):
        print("bow bow")
    def print_name(self):
        print("Dog name is:", self.name)

dog = Dog("Vijay")
dog.print_name()
dog.talk()
