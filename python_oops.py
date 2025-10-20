class car:
    wheel = 4 # class variable or static variable
    def __init__(self):
        self.mil = 10 # instance variable or name space
        self.com = "BMW"
c1 = car()
c2 = car()
c1.mil = 8
car.wheel = 5 #changing in all objects
print(c1.com, c1.mil, c1.wheel)
print(c2.com, c2.mil, c2.wheel)