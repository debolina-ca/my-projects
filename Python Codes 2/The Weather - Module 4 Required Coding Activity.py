# The Weather: Module 4 Required Coding Activity
!curl https://raw.githubusercontent.com/MicrosoftLearning/intropython/master/world_temp_mean.csv -o mean_temp.txt

# Add the weather for Rio
mean_temp_file = open('mean_temp.txt', 'a+')
mean_temp_file.write("Rio de Janeiro,Brazil,30.0,18.0\n")

# Grab the column headings
mean_temp_file.seek(0)
headings = mean_temp_file.readline()
headings_list = headings.split(',')

# Read the remaining lines from the file using a while loop
city_temp = mean_temp_file.readline()                 # assign remaining lines to a city_temp variable
while city_temp:
    each_item = city_temp.split(',')
    print(headings_list[0].title(), "of", each_item[0], headings_list[2], "is", each_item[2], "Celsius")
    city_temp = mean_temp_file.readline()

mean_temp_file.close()
