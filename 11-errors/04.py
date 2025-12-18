def divide(numbers):
    if len(numbers) <2:
        raise IndexError("at least 2 numbers are required")
    if numbers[len(numbers)-1] == 0:
        raise ValueError("last number cannot be 0")
    return numbers[0] / numbers[len(numbers)-1]

try:
    solution = divide([10, 2, 3, 4, 5])
    print(solution)
except ValueError as e:
    print(e)
except IndexError as e:
    print(e)
except Exception as e:
    print(e)
finally:
    print("finally block")

print("continue")