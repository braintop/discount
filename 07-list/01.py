names = ["john", "jane", "jim", "jill"]
print(names[0])
print(names[1])
print(names[2])
print(names[3])

names.append("jack")
print(names)
if "jane" in names:
    names.remove("jane")
    print(names)
else:
    print("jane1 not found")


names.pop()
print(names)