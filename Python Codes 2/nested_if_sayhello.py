hello = input("Enter if you want to say hello (y/n): ")
if hello.lower() == "y":
    hello_type = input("Enter if full hello or not (y/n): ")
    if hello_type.lower() == "y":
        print("Hello")
    elif hello_type.lower() == "n":
        print("Hi")
    else:
        print("That is not a correct response")
elif hello.lower() == "n":
    print("friendly nod")
else:
    print("That is not a correct response. Goodbye!!")

