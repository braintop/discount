def validate_user(**kwargs):
    if "username" not in kwargs or "email" not in kwargs:
        print("username and email are required")
    else:
        print("username and email are valid")

validate_user(username="Dana", email="dana@gmail.com", age=30)
validate_user(username="Dana")

users = [{"username": "Dana", "email": "dana@gmail.com", "age": 30},
         {"username": "John",  "age": 25},
         {"username": "Jane", "email": "jane@gmail.com", "age": 20},
         { "email": "jim@gmail.com", "age": 30},
         {"username": "Jill", "email": "jill@gmail.com", "age": 25},
         {"username": "Jack", "email": "jack@gmail.com", "age": 20},
         {"username": "Jill", "email": "jill@gmail.com", "age": 25},
         {"username": "Jill", "email": "jill@gmail.com", "age": 25},
         {"username": "Jill", "email": "jill@gmail.com", "age": 25}]
for user in users:
    validate_user(**user)

