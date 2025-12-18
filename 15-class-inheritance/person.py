class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("Person constructor finished")

    def __str__(self):
        return f"{self.name} {self.age}"
    
    def say_hello(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old")

    def pay_social_security(self):
        return 10

class Student(Person):
    def __init__(self, name, age, grade=0):
        super().__init__(name, age)
        self.grade = grade
        print("Student constructor finished")

    def say_hello(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old and my grade is {self.grade}")

    def pay_social_security(self):
        sum = 100 + super().pay_social_security()
        return sum 

p1 = Person("John", 20)
print(p1.pay_social_security())
s1 = Student("Alice", 20)
print(p1.pay_social_security())
print(s1.pay_social_security())