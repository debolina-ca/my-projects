# Ticket Check Function

def ticket_check(section, seat):
    if section.lower() == "general" or section.lower().startswith("g"):
        if seat >= 1 and seat <= 10:
            avl = True
        else:
            avl = False
    elif section.lower() == "floor" or section.lower().startswith("f"):
        if seat >= 1 and seat <= 4:
            avl = True
        else:
            avl = False
    else:
        pass
    return avl

section_1 = input("Enter preferred section (general or g, floor or f): ")
seats_1 = int(input("Enter preferred seat (1, 2, 3, .... 10): "))
print(ticket_check(section_1, seats_1))




