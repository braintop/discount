x = int(input("enter num")) 
units = x % 10 
tens = (x//10)%10 
hundreds = x//100
sum = units + tens + hundreds
print(sum)
