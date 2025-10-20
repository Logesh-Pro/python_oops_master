# meaning of instance is it belong to a particular object
#there are two types of instance methods accessor and mutator methods
class student:
    school = "Telusko"
    def __init__(self,m1,m2,m3):
        self.m2=m2
        self.m3=m3
    def avg(self):
        return (self.m1+self.m2+self.m3)/3   
    def get_m1(self): #accessor method (only fetch the value)
        return self.m1
    def set_m1(self,value): #mutator method (modify the value)
        self.m1=value 
s1 = student(34,56,78)
s2 = student(45,67,89)
print(s1.avg())
print(s2.avg())