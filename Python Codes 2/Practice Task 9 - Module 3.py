# Practice Task 9 - Module 3
# [ ] cast the long_word into individual letters list
# [ ] print each letter on a line
long_word = 'decelerating'
list_long_word = []
list_long_word = list(long_word)
print(list_long_word)


print("\n\n\n")

# [ ] use end= in print to output each string in questions with a "?" and on new lines
questions = ["What's the closest planet to the Sun", "How deep do Dolphins swim", "What time is it"]
for question in questions:
    print(question, end="?\n")

print("\n\n\n")

# [ ] print each item in foot bones
#    - capitalized, both words if two word name
#    - separated by a comma and space
#    - and keeping on a single print line
foot_bones = ["calcaneus", "talus", "cuboid", "navicular", "lateral cuneiform",
            "intermediate cuneiform", "medial cuneiform"]
for bone in foot_bones:
    print(bone.title(), end=", ")


