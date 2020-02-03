# Allergy Check: Required Coding Activity

# get user input for categories of food eaten in last 24 hours
input_test = input("Please enter categories of food eaten in the last 24 hours: ")

# print True if "dairy" is in the input_test string
print('It is',"dairy".lower() in input_test.lower(),'that "'+input_test+'" contains "dairy"')

# check the input for "nuts"
print('It is',"nuts".lower() in input_test.lower(),'that "'+input_test+'" contains "nuts"')

# check the input for "seafood"
print('It is',"Seafood".lower() in input_test.lower(),'that "'+input_test+'" contains "seafood"')

# check the input for "chocolate"
print('It is',"chocolate".lower() in input_test.lower(),'that "'+input_test+'" contains "chocolate"')
