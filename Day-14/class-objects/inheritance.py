# This is an example of Inheritance in Python !!

class first_vehical:
    def start(self):
        print("Starting Engine !!")
    def stop(self):
        print("Stopping Engine !!")
class second_vehical(first_vehical):
    def new_vehical(self):
        # super keyword is used to call the function form another class inherited !!
        super().start()
        print("Staring New Vehicalls Engine !!")
        super().stop()

shudhoo = second_vehical()
shudhoo.new_vehical()
