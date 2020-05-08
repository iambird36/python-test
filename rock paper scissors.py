me = int(input("scissors[0] rock[1] paper[2]"))
import random
com = random.randint(0, 2)
trans = ["scissors", "rock", "paper"]
print("yours:", trans[me])
print("com:", trans[com])
if me == com:
    print ("draw")
elif me == (com + 1) % 3:
    print ("i win")
else:
    print("i lose")