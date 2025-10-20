#telesco
#in python all are objects
# as of now self is for reseaving a object passed
class computer:
    def __init__(self,cpu,ram): # by defult it will call
        self.cpu= cpu  #self is used to refering the object
        self.ram= ram 
    def config(self): #self is objrct we passing
        print("Config is ", self.cpu,self.ram)
com1=computer('i5',16) #initalizing a object
com2=computer('Ryzen 3',8)
com1.config() #more simple way to call a method in class
com2.config() #config take the object before as object
# we are binding every data with a  method with respective(object) self