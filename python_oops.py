class a:
    def __init__(self):
        print("in a init")
    def feature1(self):
        print("feature 1 working")
    def feature2(self):
        print("feature 2 working")
class b:
    def __init__(self):
        print("in b init")
    def feature3(self):
        print("feature 3 working")
    def feature4(self):
        print("feature 4 working")  
class c(a,b):
    def __init__(self):
        super().__init__() #method resolution order(MRO)(left to right)(so c(a,b) a comes first so a)
        print("in c init")           
a1 = c() 