# Function: replace items in a list
three_num = [5, 3, 7, 4, 0, 3, 9, 1, 4, 4, 2, 8, 5, 4, 9, 3, 5]
index1 = int(input("Enter the index for item replacement: "))


def str_replace(int_list, index):
    if int_list[index] < 5:
        int_list[index] = "small"
    else:
        int_list[index] = "large"
    return int_list


str_replace(three_num, index1)
print(three_num)

