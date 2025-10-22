#you can create object of inner class inside the outer class or you can can create object of inner class outside the outer class provided you use outer class name to call it
class student: #outer class
    def __init__(self,name,rollno):
        self.name = name
        self.roll_no = rollno
        self.lap = self.laptop()
    def show(self):
        print(self.name,self.roll_no)
        self.lap.show()
    class laptop: #inner class
        def __init__(self):
            self.brand='hp'
            self.cpu='i5'
            self.ram='8'
        def show(self):
            print(self.brand,self.cpu,self.ram)    
s1=student("Alice",101)
s2=student("Bob",102)
s1.show()       
lap1=student.laptop()
lap2=student.laptop()
print(id(lap1))
print(id(lap2))