class student: #outer class
    def __init__(self,name,rollno):
        self.name = name
        self.roll_no = rollno
        self.lap = self.laptop()
    def show(self):
        print(self.name,self.roll_no)
    class laptop: #inner class
        def __init__(self):
            self.brand='hp'
            self.cpu='i5'
            self.ram='8'
s1=student("Alice",101)
s2=student("Bob",102)
s1.show()       
lap1=s1.lap #calling with outer class object
lap2=s2.lap
print(id(lap1))
print(id(lap2))