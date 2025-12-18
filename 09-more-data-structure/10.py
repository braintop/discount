def min_in_list(numbers):
    min_number = numbers[0]
    for number in numbers:
        if number < min_number:
            min_number = number
    return min_number

def max_in_list(numbers):
    max_number = numbers[0]
    for number in numbers:
        if number > max_number:
            max_number = number
    return max_number

numbers = [1, 2, 3, 4, 5]
x = min_in_list(numbers)
print(x)