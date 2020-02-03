# Print each word in a quote
quote = "they stumble who run fast"
start = 0
word = ""
space_index = quote.find(" ")
while space_index >= 0:
    for x in quote[start:space_index]:
        word += x
    print(word)
    word = ""
    start = space_index + 1
    space_index = quote.find(" ", space_index + 1)
for x in quote[start:]:
    word += x
print(word)

