def average_numbers(numbers):
    if len(numbers) == 0:
        raise ValueError("at least 1 number is required") 
    if not isinstance(numbers, list):
        raise TypeError("numbers must be a list")
    for number in numbers:
        if not isinstance(number, int):
            raise TypeError("numbers must be a list of integers")
    return sum(numbers) / len(numbers)

numbers = []
for i in range(10):
    num = input("enter number")
    numbers.append(int(num))
    

try:
    solution = average_numbers("5")
    print(solution)
except (ValueError, TypeError, Exception) as e:
    print(e)
finally:
    print("finally block")

print("continue")