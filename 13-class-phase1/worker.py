#worker - firstname, lastname, salary
class Worker:
    def __init__(self, firstname, lastname, salary):
        self.firstname = firstname
        self.lastname = lastname
        self.salary = salary

    def increase_salary(self, amount):
        self.salary = self.salary + amount

    def __str__(self):
        return f"{self.firstname} {self.lastname} has salary {self.salary}"

    def pay_social_security(self):
        return self.salary * 0.1

    def pay_health_insurance(self):
        return self.salary * 0.05


# w1 = Worker("John", "Doe", 1000)
# w2 = Worker("Jane", "Smith", 2000)
# if w1.salary > w2.salary:
#     print(f"{w1.firstname} {w1.lastname} has higher salary")
# else:
#     print(f"{w2.firstname} {w2.lastname} has higher salary")
# w1.increase_salary(100)
# print(w1.salary)
# print(w1.pay_health_insurance())