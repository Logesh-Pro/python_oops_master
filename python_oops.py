class computer:
    pass
c1=computer() #constuctor called internully when object created
c2=computer()
print(id(c1)) 
print(id(c2))  # every time a new object created a new memory allocated for that object.