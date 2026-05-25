# --------------------------
# -- Membership Operators --
# --------------------------
# in
# not in
# --------------------------


# String
Name = "Tarek"

print ("T" in Name) 
print ("R" in Name)
print ("f" in Name)

print("#" * 50 )
# List
friends = ["Ahmed", "Ali", "Omar", "Youssef"]
print ("Ahmed" in friends)
print ("Ali" in friends)
print ("Omar" in friends)
print ("Youssef" in friends)
print ("Tarek" in friends)

#using In and Not In with condition
coujntreyONe = ["sweda", "france", "egypt", "ksa"]
countryOneDiscount = 80

countryTwo = ["nantes", "paris", "london", "italy"]
countryTwoDiscount = 50

myCountry = "x"
if myCountry in coujntreyONe :
    print(f"Your Country Is {myCountry} And Your Discount Is {countryOneDiscount}%")
elif myCountry in countryTwo :
    print(f"Your Country Is {myCountry} And Your Discount Is {countryTwoDiscount}%")
else :
    print(f"Your Country Is {myCountry} And Your Discount Is 0%")
