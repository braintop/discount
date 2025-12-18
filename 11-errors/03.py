def divide(a, b):
    if b == 0:
        raise Exception("b cannot be 0")
    return a / b


try:
    x = divide(10, 0)
    print(x)
except Exception as e:
    print(e)
finally:
    print("finally block")

print("continue")