# List of letters
word = input("Enter a word: ")
length = len(word)
odd_letters = []
even_letters = []
for index in range(0, length, 2):
    odd_letters += word[index]
for letter in range(1, length, 2):
    even_letters += word[letter]
print(odd_letters)
print(even_letters)
