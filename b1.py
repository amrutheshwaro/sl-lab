from collections import Counter

#Read a list of elements
a = []
b = int(input("Enter the size of the list.\n"))
print("Enter the elements of the list.")
for i in range(b):
    a.append(int(input()))

#Create a new list having all the elements minus the duplicates
new_a = []
new_b = []
[new_a.append(element) for element in a if element not in new_a ] 
print("New list without duplicates", new_a)

#Use one-line comprehensions to create a new list of even numbers
even_numbers = [x * 2 for x in range(11)]
print("List of even numbers", even_numbers)

#List reversing the even_numbers elements
reverse_even_numbers = even_numbers[::-1]
print("Reversed list", reverse_even_numbers)

#Count the frequency of words in a given file
def word_count(file_path):
    with open(file_path) as f:
        return Counter(f.read().strip().split())
print("The frequency of the words in the file")
print(word_count("b1.txt"))

#Read a list of numbers. Use a recursive function to find the maximum element of n numbers
d = []
e = int(input("Enter the size of the list.\n"))
print("Enter", e, "numbers.")
for i in range(e):
    d.append(int(input()))
def Max(list):
    if len(list) == 1:
        return list[0]
    else:
        m = Max(list[1:])
        return m if m > list[0] else list[0]
print("The maximum element in the list is", Max(d))