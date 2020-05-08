#def bmi(height, weight):
#    return weight / (height / 100) ** 2

class person:
    name = None
    height = None
    weight = None

    def __init__(self, n, h, w):
        self.name = n
        self.height = h
        self.weight = w

    def return_bmi(self):
        return self.weight / (self.height / 100) ** 2

p1 = person("Elwing", 175, 75)
print(p1.name, p1.return_bmi())

p2 = person("Bob", 180, 80)
print(p2.name, p2.return_bmi())