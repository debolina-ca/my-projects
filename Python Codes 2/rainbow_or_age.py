# Rainbow or Age


str001 = input("Enter first letter of a rainbow color or enter your age: ")
def rainbow_or_age(str003):
    if str003.isdigit():
        age_20(int(str003))
    elif str003.isalpha():
        rainbow_colors(str003)
    else:
        return str003.isalpha()
import Age_20_function
import Rainbow_Colors
result1 = rainbow_or_age(str001)
print(result1)