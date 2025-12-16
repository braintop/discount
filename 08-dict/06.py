products = ("ball","apple","orange","banana","pear")
sum =0
for product in products:
    print(product*3)
    sum += len(product)


for i in range(len(products)):
    print(i, products[i]*3)


