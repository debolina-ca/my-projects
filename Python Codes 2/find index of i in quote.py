# find and display the index of all the letter i's in code_tip
code_tip = "code a conditional decision like you would say it"
location = code_tip.find("i")
while location >= 0:
    print(location)
    location = code_tip.find("i", location + 1)


