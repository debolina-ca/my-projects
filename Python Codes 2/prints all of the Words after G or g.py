# Program: Words after "G"/"g"
# prints all of the words that start with h-z
quote = input("Enter a famous quote: ")
quote = quote + " "
word = ""
start = 0
space_index = quote.find(" ")
while space_index >= 0:
    for letter in quote[start:space_index]:
        word += letter
    if word[0].lower() > "g":
        print(word.upper())
    word = ""
    start = space_index + 1
    space_index = quote.find(" ", space_index + 1)
'''for letter in quote[start:]:
    word += letter
if word[0].lower() > "g":
    print(word)
'''