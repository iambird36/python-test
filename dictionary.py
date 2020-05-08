person = {"name":"Elwing","height":175,"handsome":True}
print(person)
# 取出東西
print(person["name"])
# add weight
person["weight"] = 75
print(person)
# change value
person["height"] = 177
print(person)
person["height"] = person["height"] + 3
print(person)
del person["weight"]
print(person)
for key in person:
    print("-", key, person[key])