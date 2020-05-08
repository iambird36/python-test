times=0
f1=0
f2=0
while times < 10:
    if times == 0:
        f2=0
        f=0
    elif times == 1:
        f1 =1
        f=1
    else:
        f = f1 + f2
        f2 = f1
        f1 = f
    print("no", times + 1, f)
    times = times + 1