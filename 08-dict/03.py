import random
numbers = []
for i in range(100):
    number = random.randint(1, 200)
    numbers.append(number)
print(numbers)
number = int(input("enter number"))
if number in numbers:
    print("number found")
else:
    print("number not found")

count = int(input("enter count"))
counter = 0
#value loop 
for number in numbers:
    if number == count:
        counter += 1
        
#index loop 
for i in range(len(numbers)):
    if numbers[i] == count:
        counter += 1

print(counter)


print(counter)
