try:
    names = ["john", "jane", "jim", "jill"]
    print(names[7])

except Exception as e:
    print(e)
finally:
    print("finally block")

print("continue")
