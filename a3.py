def AtomicDictionary():
    atomic_elements = {
        "H": "Hydrogen",
        "He": "Helium",
        "Li": "Lithium",
        "Be": "Berylium"
    }

    new_symbol = input("Enter the symbol of the atomic element to be inserted.\n")
    if new_symbol in atomic_elements.keys():
        print("Entered symbol already exists in the dictionary.")
    else:
        atomic_elements[new_symbol] = input("Enter the element corresponding to the symbol " + new_symbol + ".\n")
        print("The new key value pair has been inserted into the dictionary.")
    
    print("The number of atomic elements in the dictionary is", len(atomic_elements.keys()))
    
    search_symbol = input("Enter the symbol of the element to be searched in the dictionary.\n")
    if search_symbol in atomic_elements:
        print("The entered element is present in the dictionary and the element name is", atomic_elements[search_symbol])
    else:
        print("The entered element was not found in the dictionary.")
    
    search_element = input("Enter the element name to be searched in the dictionary.\n")
    if search_element in atomic_elements.values():
        print("The entered element is present in the dictionary and the element symbol is", ''.join(map(str, [key for key, value in atomic_elements.items() if value == search_element])))
    else:
        print("The entered element name was not found in the dictionary.")
