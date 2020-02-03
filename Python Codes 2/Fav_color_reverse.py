fav_color = input("Enter your favourite color: ")
new = ""
for x in fav_color[::-1]:
    new += x
print(new + fav_color)