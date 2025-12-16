while True:
    num = int(input("enter num or 0 to exit"))
    if num==0:
        print(num%7)
        break
    if num%7==0: 
        print("divisible by 7")
    else:
        print("not divisible by 7")

print("done")
