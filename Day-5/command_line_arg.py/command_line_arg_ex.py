# This is example of environment variables pass to a progarm from command line !!

import sys

def add(num1, num2):
    A = num1 + num2
    return(A)

def sub(num1, num2):
    S = num1 - num2
    return(S)

def mul(num1, num2):
    M = num1 * num2
    return(M)

# This is how i have take comand line arguments from the user
number1 = float(sys.argv[1])
operation = sys.argv[2]
number2 = float(sys.argv[3])

if operation == "add":
    addoutput = add(number1, number2)
    print(addoutput)
if operation == "sub":
    suboutput = sub(number1, number2)
    print(suboutput)
if operation == "mul":
    muloutput = mul(number1, number2)
    print(muloutput)