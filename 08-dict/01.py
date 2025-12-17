person = {
    "name": "Dana",
    "age": 25,
    "city": "Tel Aviv"
}
print(person["name"])
print(person.get("name"))
print(person.get("name1", "Unknown"))
print(person.get("name2", "Unknown"))
keys = person.keys()
print(keys)
values = person.values()
print(values)
items = person.items()
print(items)
code = input("enter code")# code is the key 
country = input("enter country")
while code in person:
person[code] = country
print(person)
x, y = (1, "car")
for key, value in person.items():
    print(key, value)

code = input("enter code")# code is the key 
if code in person:
    print(person[code])
else:
    print("code not found")
