# Task 2 - The Weather - Create a program that reads from a file to display city name and average temperature in Celsius
!curl https://raw.githubusercontent.com/MicrosoftLearning/intropython/master/world_temp_mean.csv -o mean_temp.txt
mean_temp_file = open('mean_temp.txt', 'r')
headings = mean_temp_file.readline()
headings_list = headings.split(',')
print(headings_list)
city_temp = mean_temp_file.readlines()
print()
for item in city_temp:
    each_item = item.split(',')
    print("month ave: highest high for", each_item[0], "is", each_item[2], "Celsius")
