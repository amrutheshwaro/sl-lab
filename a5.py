from functools import reduce

#Create an list of elements
a = [1, 2, 4, 5, 8, 6]

#Multiply each element of the list by 3 using list-comprehension to create a new list
new_a = [x * 3 for x in a]

#Use lambda and reduce function to find the sum of the elements of the original list and the new list
b = reduce(lambda x, y: x + y, a)
c = reduce(lambda x, y: x + y, new_a)

#Printing the results
print("Original list:", a)
print("New list:", new_a)
print("Sum of elements of original list:", b)
print("Sum of elements of new list:", c)