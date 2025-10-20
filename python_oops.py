# meaning of instance is it belong to a particular object
#there are two types of instance methods accessor and mutator methods
class student:
    school = "Telusko"
    def __init__(self,m1,m2,m3):
        self.m2=m2
        self.m3=m3
    def avg(self):
        return (self.m1+self.m2+self.m3)/3  
    @classmethod #if we are working with a class variable or method(cls) we want to use @classmethod
    def getschool(cls): # if we are working with a class variable we want to use cls
        return cls.school
    @staticmethod # if we are not working with a class variable or method or not using anything we want to use @staticmethod
    def info():
        print("this is student class.. in abc module") #static method we dont want to use self or cls
s1 = student(34,56,78)
s2 = student(45,67,89)
print(student.getschool())
student.info()