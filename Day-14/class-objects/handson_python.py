# This is na Hands-On Session of Python [ Inheritance ]!!

class Person:
    def __init__(self, name):
        self.name = name
    def sayName(self):
        print(self.name)
class Engineer(Person):
    def __init__(self, name):
        super().__init__(name)
        self.profession = "DevOps Engineer"
    def sayProfession(self):
        print(self.profession)

shudho = Engineer("Shudhodhan")
shudho.sayName()
print("is")
shudho.sayProfession()

