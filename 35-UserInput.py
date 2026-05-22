#--------------------
# User Input
#--------------------

fName = input("what is your first name? ")
mName = input("what is your middle name? ")
lName = input("what is your last name? ")

fName = fName.strip().capitalize()
mName = mName.strip().capitalize()
lName = lName.strip().capitalize()

print("Hello " + fName + " " + mName + " " + lName + " Im Happy To See You")
