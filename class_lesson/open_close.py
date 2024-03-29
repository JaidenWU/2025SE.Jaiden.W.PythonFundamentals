# over a list of numbers
numberList = []
newNumberList = []

with open("myText.txt") as file:
    for line in file:
        numberList.append(line.strip())

for number in numberList:
    number = int(number) + 1
    number = str(number)
    newNumberList.append(number)


with open("myText.txt", "w") as file:
    for numbers in newNumberList:
        file.write(numbers)
        file.write("\n")

# just with one number
"""
with open("myText.txt") as file:
    lines = file.readlines()

number = int(lines[0]) + 1
number = str(number)

with open("myText.txt", "w") as file:
    file.write(number)
"""
