# ---------------
# -- Nested If --
# ---------------

uName = "tarek"
isStudent = "Yes"
uCountry = "x"
cName = "Python"
cPrice = 100

if uCountry == "sweda" or uCountry == "nantes" or uCountry =="paris":
    if isStudent == "Yes":
        print (f"hello {uName} becouse you are from {uCountry} and you are a student you will pay {cPrice - 30} for the course {cName}")
    else:

      print(f"Hi {uName} Because U R From {uCountry}")
      print(f"The Course \"{cName}\" Price Is: ${cPrice - 25}")
elif uCountry == "france":
    print(f"hello {uName} becouse you are from {uCountry} you will pay {cPrice - 10} for the course {cName}")
else: 
    print(f"hello {uName} because you are from {uCountry} you will pay {cPrice} for the course {cName}")