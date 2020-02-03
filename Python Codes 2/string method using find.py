# find substring in loop
work_tip = "save your code"
print("work_tip: ", work_tip, "\n")
location = work_tip.find("o")
while location >= 0:
    print ("'o' is at index =", location)
    location = work_tip.find("o", location + 1)
print("\nno more o's, -1 was returned")