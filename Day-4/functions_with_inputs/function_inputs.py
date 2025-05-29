# This is the more right way to define function in python !!
# What return keyword do here is just returns the add function
def addition(num1, num2):
    add = num1 + num2
    return add

def subtraction(num1, num2):
    sub = num1 - num2
    return sub

def multiplication(num1, num2):
    multi = num1 * num2
    return multi

print(addition(5, 10))
print(subtraction(20, 19))
print(multiplication(2, 2))