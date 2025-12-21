from abc import ABC, abstractmethod
class Animal(ABC):
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y
    
    @abstractmethod
    def make_sound(self):
        pass
    
    def move_by_x_and_y(self, dx, dy):
        self.x = self.x + dx
        self.y = self.y + dy

    def __str__(self):
        return f"{self.name} {self.x} {self.y}"


class Cat(Animal):
    def __init__(self, name, x, y):
        super().__init__(name, x, y)

    def make_sound(self):
        print("meow meow")
    def __str__(self):
        return f"{self.name} {self.x} {self.y}"

if __name__ == "__main__":
    c1 = Cat("Cat1", 10, 20)
    c1.move_by_x_and_y(10, 20)
    c1.make_sound()
    print(c1)