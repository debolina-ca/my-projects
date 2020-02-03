# Program: list-o-matic Function: Module 2 Required Coding Activity
list1 = ["cat", "tiger", "cat", "lion"]


def list_o_matic(string, list):
    if string == "":
        return list.pop(), "popped from the list"
        list.pop()
    else:
        if string in list:
            list.remove(string)
            return "1 instance of", string, "removed from list"
        else:
            list.append(string)
            return "1 instance of", string, "appended to list"


while list1:
    print("Look at all the animals ", list1)
    string1 = input("Enter the name of an animal or 'quit' to exit: ")
    if string1.lower() != "quit":
        print(list_o_matic(string1, list1))
    else:
        print("Goodbye")
        break
print(list1)
