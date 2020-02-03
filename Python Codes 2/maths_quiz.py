# create a math quiz question and ask for the solution until the input is correct
x = 5
y = 3
print("x = 5")
print("y = 3")
z = input("Enter the value of x^2 + y^3: ")
solution = x*x + y*y*y
if int(z) == solution:
    print("Correct")
else:
    print("Sorry...that's incorrect.")




