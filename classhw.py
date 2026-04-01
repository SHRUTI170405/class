# CREATE 5 CLASSES OF YOUR CHOICE  AND WRITE MINIMUM 2 ATTRIBUTES AND 1 METHOD IN EACH CLASS
#1.bus 
class Bus:
    def __init__(self, number, route):
        self.number = number
        self.route = route

    def show(self):
        print("Bus No:", self.number, " Route:", self.route)

b1 = Bus(101, "Hadapsar to Swargate")

print(b1.number)      
b1.show()      


#2.mandir
class Mandir:
    def __init__(self, name, location):
        self.name = name
        self.location = location

    def darshan(self):
        print("Visiting", self.name, "located at", self.location)

m1 = Mandir("Ganpati Mandir", "Karvenagar")


print(m1.name)
print(m1.location)
m1.darshan()


#3.vegetable
class Vegetable:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def show(self):
        print("Vegetable:", self.name, " Price :", self.price, "rs per kg")

v1 = Vegetable("Tomato", 40)
print(v1.name)
print(v1.price)
v1.show()

#4.Induction
class Induction:
    def __init__(self, brand, power):
        self.brand = brand
        self.power = power   

    def start(self):
        print("Induction of", self.brand, "has", self.power, "W power")

i1 = Induction("Prestige", 2000)
print(i1.brand)
print(i1.power)
i1.start()

#5.Watermelon
class Watermelon:
    def __init__(self, weight, price):
        self.weight = weight      
        self.price = price        

    def show(self):
        print("Watermelon Weight:", self.weight, "kg and Price is:", self.price)


w1 = Watermelon(3, 100)
print(w1.weight)
print(w1.price)
w1.show()