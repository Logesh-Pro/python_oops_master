#telesco
#in python all are objects
class computer:
    def config(self): #self is objrct we passing
        print("i5, 16gb, 512GB")
com1=computer() #initalizing a object
computer.config(com1) #we want say which object we are using
com2=computer()
computer.config(com2) #more clear way of calling a method in class
com1.config() #more simple way to call a method in class
com2.config() #config take the object before as object