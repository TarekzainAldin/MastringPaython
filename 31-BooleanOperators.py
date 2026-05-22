# -----------------------
# -- Boolean Operators --
# -----------------------
# and
# or
# not
# -----------------------
age = 36
country = "Sweda"
rank = 10

print(age> 16 and country == "sweda" and rank > 5)  # return True if all conditions are True, otherwise False
print(age >16 and country == "france" and rank > 5) # return False because the second condition is False

print(age > 40 or country == "sweda" or rank > 20 ) # return True because the second condition is True, even if the first and third conditions are False
print (age > 40 or country == 'france' or rank > 20) # return False because all conditions are False

print(age > 16)# return True because the condition is True
print(not age > 16) # return False because the condition is True and we use not