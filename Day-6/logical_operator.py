# This is the example of logical operators

a = 1
b = 1 
c = a is b # this is true so "c = true"

p = 2
q = 2
k = p is q # this is true so "k = true"

x = 3
y = 4
z = x is y # this is false so "z = flase"

ans1 = c and k
ans2 = k and z
ans3 = c or k


print("This is true bcoz c=true and k=true :",ans3)
print("This is false bcoz k=true and z=flase :",ans2)



