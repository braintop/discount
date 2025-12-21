class MathUtils:
    @staticmethod
    def add(a, b):
        if not isinstance(a, int) or not isinstance(b, int):
            raise ValueError("a and b must be integers")
        return a + b
    
    @staticmethod
    def subtract(a, b):
        return a - b
    
    @staticmethod
    def multiply(a, b):
        return a * b
    
    @staticmethod
    def divide(a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
    
    @staticmethod
    def power(a, b):
        return a ** b
    
    @staticmethod
    def square(a):
        return a ** 2

    @staticmethod
    def average(numbers):
        if not isinstance(numbers, list):
            raise ValueError("numbers must be a list")
        if len(numbers) == 0:
            raise ValueError("numbers must be a list of at least 1 number")
        return sum(numbers) / len(numbers)
    @staticmethod
    def max(numbers):
        if not isinstance(numbers, list):
            raise ValueError("numbers must be a list")
        if len(numbers) == 0:
            raise ValueError("numbers must be a list of at least 1 number")
        return max(numbers)
    @staticmethod
    def min(numbers):
        if not isinstance(numbers, list):
            raise ValueError("numbers must be a list")
