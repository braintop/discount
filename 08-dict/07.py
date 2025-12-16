names = {"john", "jane", "jim", "jill"}
for name in names:
    print(name)

for i in range(len(names)):
    print(names[i])

names.add("jack")
names.add("jack")
names.add("jack")
names.add("jack")
names.add("jack")

print(names)

names.remove("jill")