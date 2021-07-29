movies=["harry potter","spider","life","noon"]
# new=[i for i in movies if 'a' in i]
# print(new)
new=[i.replace("noon","morning") for i in movies ] 
print(new)
