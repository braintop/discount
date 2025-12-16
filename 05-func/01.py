#void - doent return value 
def sayHello(name):
    print(f"==☺️ Hello, {name} ❤️--")

def plus(a, b):
    return a + b

def print_plus(a, b):
    print(f"=={a} + {b} = {plus(a, b)}--")

def print_message():
    print("Make Things Go Right")



def print_moutliply_times(string, times):
    for i in range(times):
        print(string)

times = int(input("enter times"))
word = input("enter word")
print_moutliply_times(word, times)
print_moutliply_times(3, "Hello")

for i in range(3):
    print_message()


