#from car import Car
from math_utils import MathUtils
#print(Car.get_counter())
try:
    print(MathUtils.add(1, 2))
    print(MathUtils.subtract(1, 2))
    print(MathUtils.multiply(1, 2))
    print(MathUtils.divide(1, 0))
    print(MathUtils.power(1, 2))
    print(MathUtils.square(1))
    print(MathUtils.average([1, 2, 3, 4, 5]))
    print(MathUtils.max([1, 2, 3, 4, 5]))
    print(MathUtils.min([1, 2, 3, 4, 5]))
except ValueError as e:
    print(e)
finally:
    print("finally")

print("continue")