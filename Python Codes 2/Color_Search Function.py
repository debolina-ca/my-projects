# Program: Paint Stock
# check a list for a paint color request and print status of color "found"/"not found"


def color_search(color_request1, paint_colors = ["ivory", "beige", "lilac", "magenta", "yellow", "turquoise"]):
    for color in paint_colors:
        if color.lower() == color_request1.lower():
            return"available"
        else:
            pass
    return"unavailable"


color_request = input("Enter your color choice: ")
print(color_request.title(), "is", color_search(color_request))
