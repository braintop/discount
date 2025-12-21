#car - brand, id, color , price 
class Car:
    counter = 0
    def __init__(self, brand, id, color, price):
        self.brand = brand
        self.id = id
        self.color = color
        self.__price = price
        Car.increase_counter()
        
    @staticmethod
    def increase_counter():
        Car.counter = Car.counter + 1


    @staticmethod
    def get_counter():
        return Car.counter
    
    @property
    def id(self):
        return self.__id
    
    @id.setter
    def id(self, value):
        if len(value) < 6:
            raise ValueError("Id cannot be negative")
        self.__id = value

    @property
    def price(self):
        return self.__price
    
    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative")
        self.__price = value
    
    def __str__(self):
        return f"{self.brand} {self.__id} {self.color} {self.__price}"

try:
    c1 = Car("bmw", "1213", "Red",10)
    print(c1.price)
    print(c1.id)
    c1.price = 10.03
    print(c1)
except ValueError as e:
    print(e)
finally:
    print("finally")
