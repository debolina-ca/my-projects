# [ ] Get user input for first_name
# Program: capitalize-io
name = input("Enter first name: ")
new_name = ""
for x in name:
    if x.lower() == "i" or x.lower() == "o":
        new_name += x.upper()
    else:
        new_name += x
print(new_name)