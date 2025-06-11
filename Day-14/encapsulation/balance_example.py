# This is an example of encapsulation with variables

class Person:
    def __init__(self, name):
        self.name = name
    def sayName(self):
        print(self.name)
class Engineer(Person):
    def __init__(self, name):
        super().__init__(name)
        self.work = "Engineer"
    def whatWork(self):
        print(self.work)

p1 = Engineer("Shudhodhan")

p1.whatWork()
p1.sayName()

