# this is an example of private and public function 

class SomeFunction():
    def Public(self):
        print("This is an Public Function !!")
    def __Private(self):
        print("This is an Private Function !!")

Object1 = SomeFunction()
Object1.Public()
Object1._SomeFunction__Private()

# The above is the way to call Private funtion object 