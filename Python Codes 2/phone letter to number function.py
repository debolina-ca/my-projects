# Program: Letter to Number Function
phone_letters = [" ", "", "ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ", "*", "#"]
letter1 = input("Enter a single letter(A - Z), number (0 - 9), space or empty string: ")


def let_to_num(letter):
    key = 0
    while key < 10:
        if letter.upper() in phone_letters[key] or letter == str(key):
            if letter in phone_letters[key] and letter in phone_letters[key + 1]:
                return 1
            else:
                return key
        else:
            key = key + 1
    return "Not Found"


print(let_to_num(letter1))
