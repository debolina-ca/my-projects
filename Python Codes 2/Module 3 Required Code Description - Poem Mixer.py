# Module 3 Required Code Description - Program: Poem Mixer
poem = input("Enter a poem, verse or saying: ")
words_list = poem.split()
modified_list = []
length = len(words_list)
for index in range(length):
    if len(words_list[index]) <= 3:
        words_list[index] = words_list[index].lower()
    elif len(words_list[index]) >= 7:
        words_list[index] = words_list[index].upper()
    else:
        pass
    modified_list += [words_list[index]]


def word_mixer(modified_list):
    modified_list.sort()
    new_list = []
    while len(modified_list) > 5:
        new_list.append(modified_list.pop(-5))
        new_list.append(modified_list.pop(0))
        new_list.append(modified_list.pop(-1))
        new_list.append("\n")
    return " ".join(new_list)


print(word_mixer(modified_list))
