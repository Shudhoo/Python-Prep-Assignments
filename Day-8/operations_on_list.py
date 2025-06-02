# These are some of the operations on the list 
my_list = ["k", "c", "z", "u", "c", "f", "e", "z", "l","f","k","y","x","u"]
print(len(my_list))

# To add element to list 
my_list.append("j")
print(len(my_list),"=",my_list)

# To remove element from list
my_list.remove("c")
print(len(my_list),"=", my_list)

# To slice a list meaning create a list from the list 
new_list = my_list[0:2] # this will take upto 2 index value i.e. a,b not the element which is at the 2nd index
print("New list formed =",new_list)

# To sort the list there is another function
my_list.sort()
print("This is the sorted list =",my_list)

# this is my example
a = ["1", "2","3"]
print(a)
b = a[1]
print(b)
c = a[2]
print(c)
d = int(b) + int(c)
print(d)


# to concatinate elements
print(my_list[2] + my_list[8] + my_list[0] + my_list[5] + " " + my_list[8])

