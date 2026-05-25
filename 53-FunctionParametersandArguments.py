# ---------------------------------------
# -- Function Parameters And Arguments --
# ---------------------------------------

a,b,c = "tarek","ammar","ziad"
print(f"hello {a}")
print(f"hello {b}")
print(f"hello {c}")

print("#" * 20)


#  def                     => Function Keyword [Define]
# say_hello()             => Function Name
# name                    => Parameter
# print(f"Hello {name}")  => Task
# say_hello("tarek")      => tarek is The Argument
def say_hello(name):
    print(f"Hello {name}")

say_hello("Tarek")
say_hello("Ammar")
say_hello("Ziad")


print("#" * 20)
def say_hi(a,b,c):
    print(f"Hello {a}")
    print(f"Hello {b}")
    print(f"Hello {c}")

say_hi("Tarek","Ammar","Ziad")

print("#" * 20)

def addition(num1, num2):
    return num1 + num2

result1 = addition(10, 20)
result2 = addition(100, 200)

print(result1)
print(result2)
print("#" * 20)


def addition(num1,num2):
    if type(num1)!=int or type(num2) !=int:
        return "please enter numbers only"
    else:
        print(num1 +num2)
    
result = addition(400,350)
print(result)

print("#" * 20)

def full_name(first_name, middle_name, last_name):
    return f"{first_name.strip()} {middle_name.strip().capitalize()} {last_name.strip()}"
print(full_name("Tarek", "Ammar", "Ziad"))
 