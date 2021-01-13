#Function AtomicDictionary
def AtomicDictionary():

    #Create dictionary that contains the atomic element symbol and its name
    atomic_elements = {
        "H": "Hydrogen",
        "He": "Helium",
        "Li": "Lithium",
        "Be": "Berylium"
    }

    #Insert an element into the dictionary
    new_symbol = input("Enter the symbol of the atomic element to be inserted.\n")
    if new_symbol in atomic_elements.keys():
        print("Entered symbol already exists in the dictionary.")
    else:
        atomic_elements[new_symbol] = input("Enter the element corresponding to the symbol " + new_symbol + ".\n")
        print("The new key value pair has been inserted into the dictionary.")

    #Display the number of atomic elements in the dictionary
    print("The number of atomic elements in the dictionary is", len(atomic_elements.keys()))

    #Search an element in the dictionary using the key
    search_symbol = input("Enter the symbol of the element to be searched in the dictionary.\n")
    if search_symbol in atomic_elements:
        print("The entered element is present in the dictionary and the element name is", atomic_elements[search_symbol])
    else:
        print("The entered element was not found in the dictionary.")

    #To search a key using the value of the given element
    search_element = input("Enter the element name to be searched in the dictionary.\n")
    if search_element in atomic_elements.values():
        print("The entered element is present in the dictionary and the element symbol is", ''.join(map(str, [key for key, value in atomic_elements.items() if value == search_element])))
    else:
        print("The entered element name was not found in the dictionary.")
