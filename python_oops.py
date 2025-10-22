class a:
    def __init__(self):
        print("in a init")
    def feature1(self):
        print("feature 1 working")
    def feature2(self):
        print("feature 2 working")
class b(a):
    def __init__(self):
        super().__init__() # if we want to call super class init we have to use super()
        print("in b init")
    def feature3(self):
        print("feature 3 working")
    def feature4(self):
        print("feature 4 working")       
a1 = b() 
#sub class can't call super class init if it have init on its class