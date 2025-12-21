class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __str__(self):
        return f"{self.name} {self.salary}"

class Manager(Employee):
    def __init__(self, name, salary, department, bonus  ):
        super().__init__(name, salary)
        self.department = department
        self.bonus = bonus

    def __str__(self):
        return f"{self.name} {self.salary} {self.department} {self.bonus}"

    def total_salary(self):
        return self.salary + self.bonus

    def get_department(self):
        return self.department
e1=Employee("John", 1000)
print(e1)

m1 = Manager("John", 1000, "IT", 100)
print(m1)
print(m1.total_salary())
print(m1.get_department())
        