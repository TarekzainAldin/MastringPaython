#-----------------
#--Boolean --
#-----------------
#--Boolean --
#-----------------
#[1] in programming, we have a data type called Boolean that can only have two values: True or False.
#[2] Boolean Values Are The Two Constant Objects False + True.

name = " "

print(name.isspace()) # return True if all characters in the string are whitespace, otherwise False 

print("#" * 50)

print (1000>500) # return True if 1000 is greater than 500, otherwise False
print (1000<500) # return True if 1000 is less than 500, otherwise False
print (1000==500) # return True if 1000 is equal to 500
print(10>90 ) # return True if 10 is greater than 90, otherwise False

print("#" * 50)
#True values
print(bool("Hello")) # return True because the string is not empty
print(bool(100))
print(bool(100.95))
print(bool(True))
print(bool([1, 2, 3, 4, 5]))

print("#" * 50)
#False values
print(bool(0))
print(bool(""))
print(bool(''))
print(bool([]))
print(bool(False))
print(bool(()))
print(bool({}))
print(bool(None))