# ---------------------------
# -- Break, Continue, Pass --
# ---------------------------

myNuumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9,13,15,17,19,20]


# Continue Example
for number in myNuumbers:
    if number == 13:
        continue
    print(f"The Number Is: {number}")

print("#" * 50)

#Break Example
for numbeer in myNuumbers:
      if numbeer  == 13:
        break
print(f"Thee Number Is: {numbeer}")
print("#" * 50)


# Pass Example
for number in myNuumbers:
    if number == 13:
        pass
    print(f"The Number Is: {number}")
print("#" * 50)
