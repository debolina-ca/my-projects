# Rainbow Colors

def rainbow_colors(color):
    if color.upper() == "V":
        return " V = VIOLET"
    elif color.upper() == "I":
        return "I = Indigo"
    elif color.upper() == "B":
        return "B = Blue"
    elif color.upper() == "G":
        return "G = Green"
    elif color.upper() == "Y":
        return "Y = Yellow"
    elif color.upper() == "O":
        return "O = Orange"
    elif color.upper() == "R":
        return "R = Red"
    else:
        return "Color not found. Enter a valid color (VIBGYOR)"
color_input = input("Enter the first letter of a rainbow color (VIBGYOR): ")
result = rainbow_colors(color_input)
print(result)


    

