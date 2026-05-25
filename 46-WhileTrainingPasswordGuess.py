# ----------------------------
# -- Loop => While Training --
# -- Simple Password Guess --
# ----------------------------

tries = 4

mainPassword="tarek@1234"
inputPassword = input("Please Enter Your Password: ")
while inputPassword != mainPassword and tries > 0:
    tries -= 1
    print(f"Wrong Password, {tries} Tries Left")
    inputPassword = input("Please Enter Your Password: ")
    if tries == 0:
        print("All Tries Is Finished, Account Locked")
        break
        print("Will Not Print")
else:
        print("Password Is Correct, Welcome Back")
