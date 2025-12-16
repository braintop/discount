numbers = [12,23,5,2,6,7,40,9,10]
r = int(input("enter number"))
new_numbers = []
for number in numbers:
    if number  > r:
        new_numbers.append(number)
print(new_numbers)

