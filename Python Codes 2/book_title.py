# Get input for a book title, keep looping while input is Not in title format (title is every word capitalized)
title = ""
title = input("Enter a book title: ")
while title != title.title():
    title = input("Enter a book title: ")
print("Correct, your format is right for the book title: ", title)

