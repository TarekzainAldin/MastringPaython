# -------------------------------------
# -- Practical Your Age Full Details --
# -------------------------------------

# Input Age

age = int(input('what\'s your age?').strip())

#get age all time units

months = age* 12
weeks = age * 52
days = age * 365
hours = age * 365 * 24
minutes = age * 365 * 24 * 60
seconds = age * 365 * 24 * 60 * 60

print(f"Your Age In Months Is {months}")
print(f"Your Age In Weeks Is {weeks}")
print(f"Your Age In Days Is {days}")
print(f"Your Age In Hours Is {hours}")
print(f"Your Age In Minutes Is {minutes}")
print(f"your age in seconds is {seconds }")
