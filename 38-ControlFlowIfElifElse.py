# --------------------
# --  Control Flow  --
# -- If, Elif, Else --
# -- Make Decisions --
# --------------------
uName = "tarek"
uCountry ="sweda"
cName = "Python"
cPrice = 100

if uCountry == "sweda":
 print (f"hello {uName} becouse you are from {uCountry} you will pay {cPrice - 20} for the course {cName}")
elif uCountry == "France":
    print (f"hello {uName} becouse you are from {uCountry} you will pay {cPrice - 10} for the course {cName}")
else:
    print(f"hello {uName} because you are from {uCountry} you will pay {cPrice} for the course {cName}")