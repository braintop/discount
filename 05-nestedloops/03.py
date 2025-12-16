import random
def max1(n1, n2, n3):
    if n1 > n2 and n1 > n3:
        print("max is", n1)
    elif n2 > n1 and n2 > n3:
        print("max is", n2)
    else:
        print("max is", n3)

def max2(n1, n2, n3):
    if n1 > n2 and n1 > n3:
        return n1
    elif n2 > n1 and n2 > n3:
        return n2
    return n3

max1(1, 2, 3)
max1(4, 5, 6)
max1(7, 8, 9)

max = max2(1, 2, 3)
max =max2(4, 5, 6)
max =max2(7, 8, 9)

rnd1 = random.randint(1, 100)
rnd2 = random.randint(1, 100)
rnd3 = random.randint(1, 100)
max = max2(rnd1, rnd2, rnd3)
print("max is", max)