# -----------------
# -- Loop => For --
# -----------------
# for item in iterable_object :
#   Do Something With Item
# -----------------------------
# item Is A Vairable You Create and Call Whenever You Want
# item refer to the current position and will run and visit all items to the end
# iterable_object => Sequence [ list, tuples, set, dict, string of charcaters, etc ... ]
# ---------------------------------------------------------------
myNumbers =[1,2,3,4,5,6,7,8,9,10]
for number in myNumbers:
#    print(f"The Number Is: {number}")
    if number % 2 == 0:
        print("Even Number")
    else:
        print("Odd Number")
else:
    print("All Numbers Printed To Screen")

myName = "Tarek"
for letter in myName:
    print(f"The Letter Is: {letter}")
else:
    print("All Letters Printed To Screen")
print (myName)