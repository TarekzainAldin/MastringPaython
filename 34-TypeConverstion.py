#-------------------
#-- Type Conversion --
#------------------

#Str

a = 10
print(type(a))
print(type(str(a))) # convert the integer to a string

print("#" * 50 )

#tuple()

c = "Tarek" , #string
d = [1, 2, 3, 4, 5] # list
e={"a", "b", "c"} # set
f ={"one": 1, "two": 2} # dictionary


print(type(tuple(c))) # convert string to tuple
print(tuple(d)) # convert list to tuple
print(tuple(e)) # convert set to tuple
print(tuple(f)) # convert dictionary to tuple (only keys will be converted) 


#list()

c = "Tarek" , #string
d = [1, 2, 3, 4, 5] # list
e={"a", "b", "c"} # set
f ={"one": 1, "two": 2} # dictionary

print(type(list(c))) # convert string to list
print(list(d)) # convert list to list (no change)
print(list(e)) # convert set to list
print(list(f)) # convert dictionary to list (only keys will be converted)


print("#" * 50 )
 
# set()
c = "Tarek" , #string
d = [1, 2, 3, 4, 5] # list
e={"a", "b", "c"} # set
f ={"one": 1, "two": 2} # dictionary

print(type(set(c))) # convert string to set
print(set(d)) # convert list to set
print(set(e)) # convert set to set (no change)
print(set(f)) # convert dictionary to set (only keys will be converted)

print("#" * 50 )



d = (("A", 1), ("B", 2), ("C", 3))  # Tuple
e = [["One", 1], ["Two", 2], ["Three", 3]]  # List**

print(dict(e)) # convert list of lists to dictionary
print(dict(d)) # convert list of tuples to dictionary

print(type(dict(e))) # check type of the converted dictionary
print(type(dict(d))) # check type of the converted dictionary
