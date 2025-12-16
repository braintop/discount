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

def sum(n1, n2, n3):
    return n1 + n2 + n3

def average1(num1, num2, num3):
    avg = (num1 + num2 + num3) / 3
    return avg

def average2(num1, num2, num3):
    avg = sum(num1, num2, num3) / 3
    return avg



n1 = int(input("enter num1"))
n2 = int(input("enter num2"))
n3 = int(input("enter num3"))
x = average1(5, 8, 9)
print(x)
y = average1(40, 809, 30)
print(y)
s= (x + y) / 2
print(s)


times = int(input("enter times"))
word = input("enter word")
print_moutliply_times(word, times)
print_moutliply_times(3, "Hello")

for i in range(3):
    print_message()


