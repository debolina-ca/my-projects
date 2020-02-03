# Practice - Task 1 - Matter States
# [ ] print out the "physical states of matter" (matter_states) in 4 sentences using list iteration
# each sentence should be of the format: "Solid - is state of matter #1"
matter_states = ['solid', 'liquid', 'gas', 'plasma']
for state in range(len(matter_states)):
    print(matter_states[state], " - is state of matter #", state+1)


# Practice - Task 1 - Bird Names
# [ ] iterate the list (birds) to see any bird names start with "c" and remove that item from the list
# print the birds list before and after removals
birds = ["turkey", "hawk", "chicken", "dove", "crow"]
print(birds)
for bird in birds:
    if bird.lower().startswith("c"):
        birds.remove(bird)
print(birds)


# Practice - Task 1 - the team makes 1pt, 2pt or 3pt baskets
# print the occurrence of each type of basket(1pt, 2pt, 3pt) & total points using the list baskets
baskets = [2,2,2,1,2,1,3,3,1,2,2,2,2,1,3]
one = 0
two = 0
three = 0
for basket in baskets:
    if basket == 1:
        one += 1
    elif basket == 2:
        two += 1
    else:
        three += 1
print("Occurrence of 1pt basket =", one)
print("Occurrence of 2pt basket =", two)
print("Occurrence of 3pt basket =", three)
total_points = one*1 + two*2 + three*3
print("Total points = ", total_points)
