# -----------------
# -- Loop => For --
# --  Trainings  --
# -----------------


#Range => Range Is A Built In Function That Return A Sequence Of Numbers
#Range(start, end, step)
myRange = range(1, 11) # 1 To 10
print(myRange)
for number in myRange:
    print(f"the Range Is:{number}")

#Dictionary 
mySkills = {
    "Html": "80%",
    "Css": "70%",
    "Js": "60%",
    "Python": "90%",
    "Php": "50%"
}
print (mySkills["Python"])
print (mySkills.get("Python"))
for skill in mySkills:
    print(skill)

    print (f"my progress in {skill} is :{mySkills.get(skill)}")