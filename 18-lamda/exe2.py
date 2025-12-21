nums = [1, 2, 3, 4, 5, 6]

evens_iter = filter(lambda x: x % 2 == 0, nums)
evens = list(evens_iter)
print(evens)  # [2, 4, 6]


poitive = list(filter(lambda x: x > 0, nums))
print(poitive)

def is_positive(x):
    return x > 0

values = ["tshirt", 1,2,"book","apple",3,4,5,6,7,8,9,10]
numbers = list(filter(lambda x: isinstance(x, int) and is_positive(x), values))
print(numbers)

words = list(filter(lambda x: isinstance(x, str), values))
print(words)

