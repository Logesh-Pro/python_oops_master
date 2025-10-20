class computer:
    def __init__(self):
        self.name="logesh"
        self.age=18
    def update(self):
        self.age=30  
    def compare(self,other):
        if self.age==other.age:
            return True
        else:
            return False      
c1=computer() #constuctor called internully when object created
c2=computer()
if c1.compare(c2):
    print("They are same")
c1.name="kumar"
c1.age=20
c1.update()
if c1.compare(c2):
    print("They are same")
else:
    print("They are different")    
print(c1.name)
print(c1.age) 
print(c2.name)
print(c2.age)