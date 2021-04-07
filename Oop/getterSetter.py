class Product:
    def __init__(self,name,price):
        self.name=name
        self.__price=price         #name managaling= '_Product__price'
    
    @property
    def price(self):
        return self.__price
    
    @price.setter
    def price(self,price):
        if price>0:
            self.__price=price
    
    def __str__(self):
        return f"{self.name}=>{self.price}"

    def getPrice(self):
        return self.__price
    
    def setPrice(self,price):
        if price>0:
            self.__price=price

p=Product("Pant",1600)
print(p.name)
print(p.getPrice())
p.setPrice(300)
print(p.getPrice())
print(p.price)
p.price=500
print(p.price)
print(p)