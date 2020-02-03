# Task 8 - .join() - build a string from a list
# [ ] print a comma separated string output from the list of Halogen elements using ".join()"
halogens = ['Chlorine', 'Florine', 'Bromine', 'Iodine']
print(','.join(halogens))

# [ ] split the sentence, code_tip, into a words list
# [ ] print the joined words in the list with no spaces in-between
# [ ] Bonus: capitalize each word in the list before .join()
code_tip ="Read code aloud or explain the code step by step to a peer"
words_list = code_tip.split()
print(''.join(words_list).upper())
