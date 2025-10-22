class a:
    def feature1(self):
        print("feature 1 working")
    def feature2(self):
        print("feature 2 working")
class b:
    def feature3(self):
        print("feature 3 working")
    def feature4(self):
        print("feature 4 working")  
class c(a,b):#multiple inheritance (using class b and a methods since c is child class of b)
    def feature5(self):
        print("feature 5 working")         
a1=a()
a1.feature1()
a1.feature2()     
b1=b()
c1=c()
c1.feature1()
c1.feature3()