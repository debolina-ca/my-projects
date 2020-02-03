# Readlines Poem 2
!curl https://raw.githubusercontent.com/MicrosoftLearning/intropython/master/poem2.txt -o poem2.txt
poem2_file = open('poem2.txt', 'r')
poem2_lines = poem2_file.readlines()
count = 0
for line in poem2_lines:
    poem2_lines[count] = line[:-1]
    count += 1
print(poem2_lines)
poem2_lines.reverse()
print(poem2_lines)
