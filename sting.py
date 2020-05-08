a="hellohellohello"
b= a.replace("hello", "goodbye")
print(a)
print(b)
a = a.replace("hello", "goodbye", 2)
print(a)
# todo:
#  1) content same capital same
#  2) content same capital differernt
#  3) different

s1 = input("please enter a string1")
s2 = input("please enter a string2")
if s1 == s2:
    print("content and capital same")
elif str.lower(s1) == str.lower(s2):
    print("content same capital different")
else:
    print("different")