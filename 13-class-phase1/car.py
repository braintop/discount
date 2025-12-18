#car - brand, id, color , price 
class Car:
    def __init__(self, brand, id=0, color, price=0):
        self.brand = brand
        self.id = id
        self.color = color
        self.price = price

    def __str__(self):
        return f"{self.brand} {self.id} {self.color} {self.price}"

    def get_brand(self):
        return self.brand
    
    def increase_price(self, amount):
        self.price = self.price + amount

    def decrease_price(self, amount):
        self.price = self.price - amount


class ElectricCar(Car):
    def __init__(self, brand, id, color, price, battery_capacity):
        super().__init__(brand, id, color, price)
        self.battery_capacity = battery_capacity

    def __str__(self):
        return f"{self.brand} {self.id} {self.color} {self.price} {self.battery_capacity}"

    def charge(self, amount):
        self.battery_capacity = self.battery_capacity + amount

    def discharge(self, amount):
        self.battery_capacity = self.battery_capacity - amount


c1 = Car("dwdwd", 1212, "Red", 10.03)
c2 = Car("Toyota", 123456, "Red", 10)
s = c1.price+c2.price
print(s)
print(c1)
c1.increase_price(1000)
print(c1)
c1.decrease_price(500)
print(c1)