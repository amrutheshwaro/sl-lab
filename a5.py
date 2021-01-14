from functools import reduce

a = [1, 2, 4, 5, 8, 6]
new_a = [x * 3 for x in a]

b = reduce(lambda x, y: x + y, a)
c = reduce(lambda x, y: x + y, new_a)

print("Original list:", a)
print("New list:", new_a)
print("Sum of elements of original list:", b)
print("Sum of elements of new list:", c)