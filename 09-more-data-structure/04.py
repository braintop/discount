numbers = [12,23,5,2,6,7,40,9,10]
r = 40
for number in numbers:
    if r in numbers:
        numbers.remove(r)
print(numbers)

# for i in range(len(numbers)):
#     if numbers[i] == r:
#         numbers.remove(r)
# print(numbers)

