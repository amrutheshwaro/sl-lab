#Create list with inputs from user
a = []
b = int(input("Enter the size of the list.\n"))
print("Enter", b, "numbers.")
for i in range(b):
    a.append(int(input()))

#Determine minimum and maximum elements in the list
print("Maximum element in the list is", max(a))
print("Minimum element in the list is", min(a))

#Insert new element into the list
new_element = int(input("Enter the new element to be inserted.\n"))
pos = int(input("Enter the index where the new element is to be inserted.\n"))
a.insert(pos, new_element)
print(a)

#Delete an element from the list
ch = int(input("Enter 1 to delete by element or 0 to delete by position.\n"))
if ch == 1:
    del_element = int(input("Enter the element to be deleted from the list.\n"))
    a.remove(del_element)
else:
    pos = int(input("Enter the index of the element to be deleted.\n"))
    del a[pos]
print(a)

#Determine if an element is present in the list
find_element = int(input("Enter the element to be searched.\n"))
if find_element in a:
    print("The index of the element in the list is", a.index(find_element))
else:
    print("The element wasn't found in the list.")
