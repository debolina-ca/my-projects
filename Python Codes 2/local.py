element_list = []
element = input("Enter the name of an element: ")
while element.lower() in element_list:
    print(element.title(), "was already entered           <-- no duplicates allowed")
    element = input("Enter the name of an element: ")
while element == "":
    element = input("Enter the name of an element: ")
for count in range(4):
    element_list.append(element.lower())
    count += 1
    element = input("Enter the name of an element: ")
    while element.lower() in element_list:
        print(element.title(), "was already entered           <-- no duplicates allowed")
        element = input("Enter the name of an element: ")
    while element == "":
        element = input("Enter the name of an element: ")
element_list.append(element.lower())
print(element_list)



