def pre_word(word_1):
    if word_1.lower().startswith("pre"):
        if word_1.lower().isalpha():
            print("True")
        else:
            print("False")
    else:
        print("False")

word_2 = input("enter a word that starts with \"pre\": ")
pre_word(word_2)
print()


