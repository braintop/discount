import time
import threading

def print_numbers():
    for i in range(10):
        print(i)
        time.sleep(2)
#print_numbers()
def say_hello():
    for i in range(10):
        print("hello", i)
        time.sleep(1)
t1 = threading.Thread(target=print_numbers)
t2 = threading.Thread(target=say_hello)

t1.start()
t1.join()
t2.start()


print("continue...")

