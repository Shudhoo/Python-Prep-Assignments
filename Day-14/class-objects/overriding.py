# this is an overriding function in Python 
class A:
    def say_hi(self):
        print("Hi from A")
class B(A):
    def say_hi(self):
        print("Hi from B")

shudho = B()
shudho.say_hi()