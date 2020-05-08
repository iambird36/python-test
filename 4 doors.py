import random
win=0
lose=0
doors_number= int(input("how many doors?")
for times in range(0, 1000):
    doors = ["goat"* (doors_number -1 )]
    c = random.randint(0, len(doors) -1)
    doors.insert(c, "car")
       #choice 1 door
    c = random.randint(0,len(doors)-1 )
    del doors[c]
    doors.remove("goat")
  #  print(doors)
    c = random.randint(0, len(doors)- 1)
    if doors[0] == "car":
        win = win + 1
      #  print("win")
    else:
        lose = lose + 1
     #   print("lose")
print("win", win, "lose", lose)
total = win + lose
print("win probabilty", win / total * 100, "%")
print("lose probabilty", lose / total * 100, "%")