# -------------------------------------------------
# -- Function Packing, Unpacking Arguments *Args --
# -------------------------------------------------

print (1, 2, 3, 4, 5)

myList=[1, 2, 3, 4, 5]

print (myList)
print(*myList)

print ("#" * 50)

def say_hello(*names):
    for name in names:
        print(f"Hello {name}")

say_hello("Tarek", "Ammar", "Ziad")

def show_details(name,*skills):
    print(f"Hello {name} Your Skills Is:")
    for skill in skills:
        print(f"-{skill}")

show_details("Tarek", "Html", "Css", "Js")
show_details("Ammar", "Python", "Django")
