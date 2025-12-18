names = ["john", "jane", "jim", "john"]
first , *middle, last = names
print(first)
print(middle)
print(last)
print(middle[0])
for name in middle:
    print(name, end=", ")