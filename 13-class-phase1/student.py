class Student:
    #phase 1 - constructor
    def __init__(self, name, age):
        self.name = name
        self._age = age

     @property
     def age(self):
        return self._age

     @age.setter
     def age(self, value):
        if value < 0:
            print("Age cannot be negative")
            return
        self._age = value

s1=Student("Alice", 30)
print(s1.name)
print(s1.age)
s.age = -10 
print(s1.age)

