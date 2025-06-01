# This is example of if-statements
import sys

type = sys.argv[1]

if type == "t2.micro":
    print("we are ready to launch instance", type)
# this is if statement only executes when the condition becomes true !!
else:
    print("can't create we only create instance t2.micro not", type)