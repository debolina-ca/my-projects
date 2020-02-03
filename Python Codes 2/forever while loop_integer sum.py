# Module 4 Practice Notebook 7
sum = 0
num = input("enter an integer: ")
while num.isdigit():
    sum = sum + int(num)
    num = input("enter another integer: ")
print("Sorry you have entered a non digit. The sum of the previous integers is: ", sum)



