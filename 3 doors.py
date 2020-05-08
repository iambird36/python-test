import random
win=0
lose=0
for times in range(0, 100000):
    # prepare 3 doors
    doors = ["goat", "goat"]
    c = random.randint(0,2)
    doors.insert(c, "car")
  #  print(doors)
    # choice one door
    c = random.randint(0,2)
 #   print("choice", doors[c])
    del doors[c]
 #   print("remaining", doors)
    # remove one goat
    doors.remove("goat")
#    print("final remaining", doors)
    # check result
    if doors[0] == "car":
        win = win + 1
  #      print("win")
    else:
        lose = lose + 1
 #       print("lose")
print("win", win,"lose", lose)
total = win + lose
print("win probabilty", win /total * 100,"%")
print("lose probabilty", lose /total * 100,"%")