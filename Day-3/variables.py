# This is file where python is variables are explained !!
ec2_instance_name = "project_ec2_instance"
print(ec2_instance_name)
print(ec2_instance_name)
print(ec2_instance_name)
print(ec2_instance_name)
print(ec2_instance_name)
# If we have not used variable here and print the line 5 times
# we have to chnge this line 5 times 
# using variables we can do it just by updating single name

# Variables are of 2 types
# Global Variables
# Local Variables

# Global Scope variables are the variable which are declared outside a function 
# and Local Scope variables are the variables declared inside a function

# Example
# 
# Global Variable this are declared outside the function
a = 10
b = 5

def addition():
    # Declaring varaibles here will make it avaibale to this addition function only 
    # a = 10
    # b = 5
    print(a + b)
def subtraction():
    print(a - b)

addition()
subtraction()