# Program: adding_report() function - Final Project Required Coding Activity


def adding_report(report_type):
    total = 0
    items = ""
    while True:
        num = input('Input an integer to add to the total or input "Q" to Quit: ')
        while num.isdigit() == False and num.upper() != "Q" and num.upper().startswith("Q") == False:
            print("input is invalid")
            num = input('Input an integer to add to the total or input "Q" to Quit: ')
        if num.isdigit():
            total = total + int(num)
            if report_type.upper() == "A":
                items = items+"\n"+num
        elif num.upper() == "Q" or num.upper().startswith("Q"):
            if report_type.upper() == "A":
                print("Items: ", items)
                print("Total: ", total)
            if report_type.upper() == "T":
                print("Total: ", total)
            break
        else:
            pass


report_type_1 = input('Choose Report Type ("A" or "T")\nReport Types include All Items ("A") or Total Only ("T"): ')
while report_type_1.upper() != "A" and report_type_1.upper() != "T":
    print("input is invalid")
    report_type_1 = input('Choose Report Type ("A" or "T")\nReport Types include All Items ("A") or Total Only ("T"): ')
adding_report(report_type_1)



