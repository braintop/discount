# def print_user(**kwargs):
#     for key, value in kwargs.items():
#         print(key, value)

#print_user(name="Dana", age=30, city="Tel Aviv", country="Israel", is_student=True)
def products(**kwargs):
    for key, value in kwargs.items():
        print(key, value)

products(name="ball", price=10, in_stock=True)