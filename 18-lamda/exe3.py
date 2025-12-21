nums = [1, 2, 3, 4, 5, 6, 7, 8]
doubled_evens = [x*x for x in nums if x % 2 == 0]
print(doubled_evens)

doubled = list(map(lambda x: x*x, nums))
doubled_evens = list(map(lambda x: x*x, filter(lambda x: x % 2 == 0, nums)))


print(doubled_evens)

