# String Analysis Function

def str_analysis(str):
    if str.isdigit():
        str = int(str)
        if str > 99:
            print(str, "is a big number")
        else:
            print(str, "is a small number")
    elif str.isalpha():
        print(str, "is all alpha")
    else:
        print(str, "is neither alpha nor digit")

str_usr = input("Enter a string: ")
str_analysis(str_usr)

