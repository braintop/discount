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