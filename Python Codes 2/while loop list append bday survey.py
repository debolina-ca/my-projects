# Birthday Survey with while loop .append()
bday_survey = []
bday = input('Enter the day of the month you were born (1-31) or "q" to finish: \n')
while bday.lower() != "q":
    if int(bday) >= 1 and int(bday) <= 31:
        bday_survey.append(bday)
    else:
        print("Invalid date")
    bday = input('Enter the day of the month you were born (1-31) or "q" to finish: \n')
print(bday_survey)