# ------------------------
# -- Dictionary Methods --
# ------------------------

# setdefault()
user = {
  "name": "Tarek",
  "age": 36,
  "country": "Sweda",
  }

print(user)


print(user.setdefault("age", 25 ))
print(user.setdefault("skills", ["Html", "Css", "JS"]))
print(user)


print("#" *50 )

#popitem()

member= {
    "name": "Tarek",
    "age": 36,
    "country": "Sweda",
    "skills": ["Html", "Css", "JS"],
    "rating": 10.5
}
print(member)
member.update({"country": "france"})
print(member.popitem()) #retrun for me the last item and remove it from the dictionary

#Items()
View = {
    "name": "Tarek",
    "skill":"Xbox"}

allItems = View.items()
print(View)
View["age"] = 36
print(allItems) # return all items in the dictionary as a list of tuples
View.clear() # clear the dictionary
print(View)

print ("#" *50 )

#fromkeys()

a= ('myKeyOne', 'myKeyTwo', 'myKeyThree')
b= 'X'
print(dict.fromkeys(a,b)) # create a new dictionary with keys from a and values from bBoolean