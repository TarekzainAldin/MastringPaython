# ------------------------
# -- Dictionary Methods --
# ------------------------

# clear()

user = {
  "name": "Tarek"}
print(user)
user.clear()
print(user)
print("#" *50)

#Update()
user = {
  "name": "Tarek"}
print(user)
user.update({"age": 25})
print(user)

#copy()
main={
    "name": "Tarek",
    "age": 36,
    "country": "Sweda",
    "skills": ["Html", "Css", "JS"],
    "rating": 10.5
}
b=main.copy()
print(b)
print(b["skills"][0])
main.update({"skills": ["Python"]})
print(main)
print(b)

#Keys() + Values()
print(main.keys())
print(main.values())
