# Task 7 - Converting a string to a list with .split()
# [ ] split the string, daily_fact, into a list of word strings: fact_words
# [ ] print each string in fact_words in upper case on it's own line
daily_fact = "Did you know that there are 1.4 billion students in the world?"
fact_words = daily_fact.split()
for word in fact_words:
    print(word.upper())


# [ ] split poem on "b" to create a list: poem_words
# [ ] print poem_words by iterating the list
poem = "The bright brain, has bran!"
poem_words = poem.split("b")
for word in poem_words:
    print(word)