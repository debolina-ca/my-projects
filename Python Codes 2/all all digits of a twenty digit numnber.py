# add the digits

# create a 20 digit string, and cast to a list then add all the digits as integers, print the equation and answer

# Hint: use cast to sum the digits, and .join() to create the equation (1+2+3+...)

twenty_digit = "57956736903185670000"
twenty_digit_list = list(twenty_digit)
print(twenty_digit_list)
sum = 0
for num in twenty_digit_list:
    sum += int(num)
print("+".join(twenty_digit_list), "=", sum)




