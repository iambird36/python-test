import random
def generate_ticket():
    ticket = set()
    while len(ticket) < 6:
        n = random.randint(1, 49)
        ticket.add(n)
    return ticket
prize = generate_ticket()
print("com", prize)
times = 0
#無窮迴圈,手動停止(break)
while True:
    lottery = generate_ticket()
    print("yours", lottery)
    times = times + 1
    total = 0
    for n in lottery:
        if n in prize:
            print(n, "中了")
            total = total + 1
    print("中了", total)
    if  total >= 3:
        break
print("com", prize)
print("總共買了", times)