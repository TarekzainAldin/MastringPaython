# ---------------------------------
# -- Function Default Parameters --
# ---------------------------------

def say_hello (name = "Unknown", age = "Unknown", country = "Unknown"):
    print(f"Hello {name} your age is {age} and you live in {country}")

say_hello("Tarek", 30, "Sweda")
say_hello("Ammar", 25)
say_hello("Ziad")
say_hello()