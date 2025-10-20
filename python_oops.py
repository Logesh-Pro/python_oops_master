class Dog:
    def __init__(self,name,breed,owner):
        self.name = name
        self.breed = breed
        self.owner = owner
    def bark(self):
        print("whoof")
class Owner:
    def __init__(self,name,address,contact_number):
        self.name = name
        self.address = address
        self.phone_number = contact_number
owner1= Owner("John Doe","123 Street","555-1234")
dog1 = Dog("Buddy","Labrador",owner1)
dog1.owner.name
print(dog1.owner.name)  
owner2= Owner("Jane Smith","456 Avenue","555-5678")
dog2 = Dog("Max","Beagle",owner2)
print(dog2.owner.name)