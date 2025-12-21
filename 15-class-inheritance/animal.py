class Animal: 
    def __init__(self, name):
        self.name = name
    
    def make_sound(self):
        print("bip bip")
    
    def __str__(self):
        return f"{self.name}"

class Dog(Animal):

    def __init__(self, name, is_bite):
        super().__init__(name)
        self.is_bite = is_bite
    
    def make_sound(self):
        super().make_sound()
        print("bap bap")

    def bark(self):
        print("woof woof")

    def __str__(self):
        return f"{self.name} {self.is_bite}"

    def f(self):
        self.make_sound()
        super().make_sound()
    

d1 = Dog("Rex", True)# d1 is variable, d1 is an object of class Dog, d1 is an instance of class Dog
d1.make_sound()
d1.bark()
d2 = Dog("Rex22222", False)

a1 = Animal("Animal1")
a1.make_sound()
print(d1)