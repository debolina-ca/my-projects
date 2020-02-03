# Long Number
long_num = ""
int_num = input("enter a digit: ")
while int_num.isdigit() == True:
    long_num = long_num + int_num
    int_num = input("enter another digit: ")
print("long number: ", long_num)

