# Element_Quiz: Final Project Required Coding Activity


# Create get_names() Function to collect input of 5 unique element names
def get_names():
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
    return element_list

# import the file into the Jupyter Notebook environment
!curl https://raw.githubusercontent.com/MicrosoftLearning/intropython/master/elements1_20.txt -o elements1_20.txt
first_20_elements_file = open('elements1_20.txt', 'r')
# read one line at a time to get element names
# remove any whitespace (spaces, newlines) and save each element name, as lowercase, into a list
first_20_list = []
# print(first_20_elements_file.read())
for count in range(20):
    element_name = first_20_elements_file.readline().strip()
    first_20_list.append(element_name.lower())
print("list any 5 of the first 20 elements in the Period table")
# Call the get_names() function
element_list_input = get_names()
print(element_list_input)
# check if responses are in the list of elements
correct_responses = []
incorrect_responses = []
for item in element_list_input:
    if item in first_20_list:
        correct_responses += [item]
    else:
        incorrect_responses += [item]
percentage = len(correct_responses)*100/5
print(percentage, "% correct")
print("Found: ", correct_responses)
print("Not Found", incorrect_responses)
