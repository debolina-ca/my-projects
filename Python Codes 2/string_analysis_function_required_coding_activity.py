# Program: str_analysis() Function - Module 4 Required Coding Activity
str_usr = input("enter word or integer: ")
while str == "":
    str_usr = input("enter word or integer: ")
def str_analysis(str):
    if str.isalpha():
        print(str, "is all alpha")
    elif str.isdigit():
        str = int(str)
        if str > 99:
            print(str, "is a pretty big number")
        else:
            print(str, "is smaller than expected")
    else:
        print(str, "is neither all alpha nor all digit character")
str_analysis(str_usr)
