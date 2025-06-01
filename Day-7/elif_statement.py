# this is an example of elif statement !

import sys

type = sys.argv[1]

if type == "t2.micro":
    print("creating", type ,"you will be charged 1.50$/day")
elif type == "t2.medium":
    print("creating", type, "you will be charged 2$/day")
elif type == "t2.small":
    print("creating", type, "you will be charged 2.50$/day")
else:
    print("we don't provide this instance type...sorry !!")