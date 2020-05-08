import random
# prepare 3 doors
doors = ["goat", "goat"]
c = random.randint(0,2)
doors.insert(c, "car")
print(doors)