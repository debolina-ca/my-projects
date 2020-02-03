# Animal Names Program

num_animals = 1
all_animals = ""
while num_animals <= 4:
    animal_name = input("Enter the name of an animal or enter 'exit' to escape: ")
    if animal_name.lower() == "exit":
        break
    else:
        all_animals = all_animals + " " + animal_name
    num_animals += 1
if all_animals == "":
    print ("no animals")
else:
    print("Names of all animals are: ", all_animals.title())





