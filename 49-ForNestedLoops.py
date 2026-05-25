# -----------------
# -- Loop => For --
# -- Nested Loop --
# -----------------

peoples = ["Tarek", "Osama", "Ahmed", "Sayed"]
skills = ["Html", "Css", "Js"]
for name in peoples:
    print(f"{name} Skills Is:")
    for skill in skills:
        print(f"- {skill}")


#Dictionary
peoplesAndSkills = {
 "tarek":{"html": "80%", "css": "70%", "js": "60%"},
 "osama":{"html": "90%", "css": "80%", "js": "70%"},
 "ahmed":{"html": "70%", "css": "60%", "js": "50%"},
 "sayed":{"html": "60%", "css": "50%", "js": "40%"}
}
for name in peoplesAndSkills:
    print(f"{name} skills is:")
    for skill in peoplesAndSkills[name]:
        print(f"- {skill} => {peoplesAndSkills[name][skill]}")
