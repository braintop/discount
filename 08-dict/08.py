products = {
    123: "ball",
    456: "apple",
    789: "orange",
    101: "pear",
    112: "pineapple"
}
code = int(input("enter code"))
while code in products:
    print(products[code])
    code = int(input("enter other code"))
    
products[code] = input("enter product")
print(products)

for key, value in products.items():
    print(f"product : {key} - product name:{value}")


for key in products:
    print(f"product : {key} - product name:{products[key]}")


code = int(input("enter code"))
if code in products:
    del products[code]
else:
    print("code not found")