# This is an axample of function overloadig

def addition(typeofinstance, *args):
    if typeofinstance == 'int':
        result=0
    if typeofinstance == 'str':
        result=""
    for i in args:
        result+=i
    return result
print(addition('int',3,4,5))
print(addition('str', "a", "b", "c"))
