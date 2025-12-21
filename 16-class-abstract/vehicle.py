from abc import ABC, abstractmethod
class Vehicle(ABC):
    def __init__(self, brand):
        self.brand = brand

    @abstractmethod
    def max_speed(self):
        pass

class Car(Vehicle):
    def __init__(self, brand, engine_volume, doors  ):
        super().__init__(brand)
        self.engine_volume = engine_volume
        self.doors = doors
    
    def max_speed(self):
        if self.engine_volume <2000:
            return 180
        elif self.engine_volume >=2000:
            return 220

class Bike(Vehicle):
    def __init__(self, brand, bike_type, has_engine):
        super().__init__(brand)
        self.bike_type = bike_type
        self.has_engine = has_engine
    
    def max_speed(self):
        if not self.has_engine:
            return 25
        elif self.bike_type == "electric":
            return 45
        elif self.bike_type == "road":
            return 120
        elif self.bike_type == "sport":
            return 280

        return 0

if __name__ == "__main__":
    vehicles = [Car("Toyota", 1500, 4), Bike("Honda", "electric", True), Bike("Yamaha", "sport", False), Bike("Suzuki", "road", True)]
    for vehicle in vehicles:
        print(vehicle.brand, vehicle.max_speed())