# Merge & Sort Animals
animals = ["Lion", "Tiger", "Elephant"]
add_animals = []
animal = input('Enter an animal or enter or enter empty string "" to quit: ')
while animal != "":
    add_animals += [animal.title()]
    animal = input('Enter an animal or enter or enter empty string "" to quit: ')
animals.extend(add_animals)
choice = int(input("Enter '0' if list to be displayed in alpha order or enter '1' if list to be displayed in reverse alpha order: "))
if choice == 0:
    animals = sorted(animals)
    print(animals)
elif choice == 1:
    animals = sorted(animals)
    animals.reverse()
    print(animals)
else:
    print("Invalid choice")
