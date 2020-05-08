name_set = {"周", "林", "黃", "周"}
print(name_set)

name_set.add("王")
print(name_set)

name_set.discard("王")
name_set.discard("張")
print(name_set)

name_set = name_set.union({"何", "周"})
print(name_set)

for result in name_set:
    print("-",result)