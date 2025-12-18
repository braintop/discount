names = ["john", "jane", "jim", "jill"]
for name in names:
    print(name, end=", ")

for i in range(len(names)):
    print(i, end=", ")

for i, name in enumerate(names, start=1):
    print(i, name, end=", ")

