def is_even1(num):
    if num % 2 == 0:
        print("even")
    else:
        print("odd")
    
def is_even2(num):
    if num % 2 == 0:
        return True
    else:
        return False

def is_even3(num):
    return num % 2 == 0


answer=is_even2(2)
print(answer)

if is_even2(2):
    print("send whats app")
else:
    print("send email")
