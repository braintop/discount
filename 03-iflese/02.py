grade = int(input("enter grade"))
if grade>=0 and grade<=100:
    if grade>=60:
        print("Pass")
    else:
        print("F")
else:
    print("invalid grade")