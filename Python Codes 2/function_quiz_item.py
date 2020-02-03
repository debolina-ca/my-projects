# Function: Quiz Item
question_1 = "What's the capital of Canada? "
question_2 = "Name the main city in Nova Scotia? "
question_3 = "Material from which animal is widely used to keep warm in Canada? "
solution_1 = "a"
solution_2 = "b"
solution_3 = "c"
def quiz_item(question, solution):
    answer = input(question)
    while answer != solution:
        print("Incorrect answer.")
    print("Correct answer!!!")
quiz_item(question_1, solution_1)


