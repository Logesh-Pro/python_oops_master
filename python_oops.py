class a:
    def show(self):
        print("in a show")
class b(a):
    def show(self):
        print("in b show")        
a1=b()
a1.show()        