# 1. class and object
# 2. inheritance
# 3. encapsulation
# 4. polymorphism
# 5. abstraction
# 6. accessor and mutator function
# 7. access modifier (public, private, protected)


# 1.class and object
        # ->noun
    #-> state(characterstics, property)
        # ->adjective
    # -> behaviour(action,function)
        # ->verb

# car,
#       color,model,manuf_year,
#       start, stop, run



# #Example 1
# class Car():        #brackets optional
    
#     def __init__(self,name,color,year):
#         self.name=name
#         self.color=color
#         self.year=year
    
#     def start(self):
#         print(f"{self.name} started")
    
#     def stop(self):
#         print(f"{self.name} stopped")

# c=Car("bmw","red","1984")
# c.printCarName()
# print(c.__dict__)




# #Example 2
# class Laptop:

#     def __init__(self,name,brand,ram="2gb"):
#         #instance variable
#         self.name=name
#         self.brand=brand
#         self.ram=ram
    
#     #instance method
#     def reboot(self):
#         print(f"{self.name} Laptop is rebooting.")

# msi=Laptop("6QF Leopard Pro","Msi","8gb")
# print(msi.ram)
# msi.reboot()

# dell=Laptop("2QF Tiger Pro","Dell")
# print(dell.ram)
# dell.reboot()




# #Example 3
# class Calculator:
#     def __init__(self,num1,num2):
#         self.num1=num1
#         self.num2=num2
    
#     def add(self):
#         print(f"the sum of {self.num1} and {self.num2} is {self.num1+self.num2}")
    
#     def difference(self):
#         print(f"the difference of {self.num1} and {self.num2} is {self.num1-self.num2}")
    
#     def product(self):
#         print(f"the product of {self.num1} and {self.num2} is {self.num1*self.num2}")

#     @staticmethod
#     def square_root(num):
#         return num**0.5

# cal=Calculator(2,3)
# cal.add()
# cal.difference()
# cal.product()
# print(cal.square_root(3))
# print(Calculator.square_root(5))




#Example 4
class Student:
    #class variable or static variable
    college_name="Softwarica"

    def __init__(self,id,name,address):
        self.id=id
        self.name=name
        self.address=address
    
    def printCollegeName(self):
        print("the college name is",self.college_name)

s=Student("01","Ram","Ktm")
print(s.id,s.name,s.address)
print(s.college_name)
print(s.__dict__)
s.printCollegeName()
print(f"your college name is {Student.college_name}")