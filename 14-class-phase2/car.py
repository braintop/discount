#car - brand, id, color , price 
class Car:
    def __init__(self, brand, id, color, price):
        self.brand = brand
        self.id = id
        self.color = color
        self.price = price

    @property
    def price(self):
        return self.__price
    
    @price.setter
    def price(self, value):
        if value < 0:
            print("Price cannot be negative")
            return
        self.__price = value

c1 = Car("bmw", 1212, "Red",10)
c1.price = 10.03
print(c1._price)
