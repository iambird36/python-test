# 預設值(所有右邊的參數都要有預設值
def add(n1, n2, n3 = 1, n4 = 1):
    return (n1 + n2) / n3 * n4
print(add(3, 5))
print(add(3, 5, 2))
print(add(3, 5, n4 = 2))

#print(add("hello", "world"))

def add_multiple(*nlist):
    result = 0
    for n in nlist:
        result = result + n
    return result
print(add_multiple(3,5,6))