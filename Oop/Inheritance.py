#while inheritance it must follow child class "IS A" parent class rule. self,


# #Example1
# class Person:
#     def __init__(self,name,address,contact):
#         self.name=name
#         self.address=address
#         self.contact=contact
    
#     def walk(self):
#         print(f"{self.name} is walking.")

# class Student(Person):
#     def __init__(self,name,address,contact):
#         super().__init__(name,address,contact)

# class Teacher(Person):
#     def __init__(self,name,address,contact):
#         super().__init__(name,address,contact)

# aamec=Student("Aamec","Ktm","98123123")
# print(aamec.name)
# print(aamec.address)
# print(aamec.__dict__)
# aamec.walk()

# t=Teacher("Shyam","Pkr","12387128")
# t.walk()




#Example2
class Bird:
    def __init__(self,name):
        self.name=name
    
    def fly(self):
        print(f"{self.name} is flying.")

class Pigeon(Bird):
    def __init__(self,name):
        super().__init__(name)

class Ostrich(Bird):
    def __init__(self,name):
        super().__init__(name)
    
    def fly(self):
        print(f"{self.name} cant fly")

class HummingBird(Bird):
    def __init__(self,name):
        super().__init__(name)
    
    def fly(self):
        super().fly()
        print(f"It can fly backwards also")

p=Pigeon("Pigeon")
p.fly()
o=Ostrich("Ostrich")
o.fly()
h=HummingBird("HummingBird")
h.fly()
