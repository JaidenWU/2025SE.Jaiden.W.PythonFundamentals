# implement menu UI
import csv


def main():
    studentList = []
    loadStudentData(studentList)
    while True:
        print("\nWelcome to Student Grade Management\n")
        displayMenu()
        choice = input("\nWhat's your choice? ")
        if selection(choice, studentList):
            break


def selection(choice, studentList):
    if choice == "1":
        addStudent(studentList)
    elif choice == "2":
        recordGrade(studentList)
    elif choice == "3":
        averageGrade(studentList)
    elif choice == "4":
        listStudent(studentList)
    elif choice == "5":
        saveStudentData(studentList)
        print("Thanks for using!")
        return True
    else:
        print("Invalid Choice. Try Again")


def displayMenu():
    print("1) Add a Student")
    print("2) Record Grades")
    print("3) Calculate Average Grade")
    print("4) List all Students")
    print("5) Exit")


def loadStudentData(studentList):
    with open("studentGrades.csv") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            studentList.append(
                {
                    "Student ID": row["Student ID"],
                    "Name": row["Name"],
                    "Grade": int(row["Grade"]),
                }
            )
    return studentList


def saveStudentData(studentList):
    with open("studentGrades.csv", "w") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=["Student ID", "Name", "Grade"])
        writer.writeheader()
        for student in studentList:
            writer.writerow(student)


def addStudent(studentList):
    studentAdd = input("Who are you adding? ")
    id = input("What's their ID? ")
    studentList.append({"Student ID": id, "Name": studentAdd, "Grade": []})
    print("Successfully Added!")
    saveStudentData(studentList)


def recordGrade(studentList):
    gradeStudent = input("Who are you grading? ")
    grade = int(input("What grade are you giving them "))
    for student in studentList:
        if student["Name"] == gradeStudent:
            student["Grade"] = int(grade)
    print("Successfully added grade!")
    saveStudentData(studentList)


def averageGrade(studentList):
    totalGrade = sum(student["Grade"] for student in studentList)
    averageGrade = totalGrade / len(studentList)
    print(f"Average Grade:{averageGrade:.2f}")


def listStudent(studentList):
    print("\n=== List of All Students ===")
    for student in studentList:
        print(
            f"Student ID: {student['Student ID']}, Name: {student['Name']}, Grade: {student['Grade']}"
        )


if __name__ == "__main__":
    main()
