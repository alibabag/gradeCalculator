def calculate_grade(line):
    line = line.strip()  # Remove leading/trailing whitespace
    parts = line.split(":")  # Split student name and grades
    student_name = parts[0]
    grades = parts[1].split(",")
    
    grade1 = int(grades[0])
    grade2 = int(grades[1])
    grade3 = int(grades[2])
    
    average = (grade1 + grade2 + grade3) / 3
    
    if average >= 90 and average <= 100:
        letter = "AA"
    elif average >= 85 and average <= 89:
        letter = "BA"
    elif average >= 80 and average <= 84:
        letter = "BB"
    elif average >= 75 and average <= 79:
        letter = "CB"
    elif average >= 70 and average <= 74:
        letter = "CC"
    elif average >= 65 and average <= 69:
        letter = "DC"
    elif average >= 60 and average <= 64:
        letter = "DD"
    elif average >= 50 and average <= 59:
        letter = "FD"
    else:
        letter = "FF"
        
    return f"{student_name}: {letter}\n"  # Return formatted string


def read_averages():
    with open("exam_grades.txt", "r", encoding="utf-8") as file:
        for line in file:
            print(calculate_grade(line))


def enter_grades():
    first_name = input("Student first name: ")
    last_name = input("Student last name: ")
    grade1 = input("Grade 1: ")
    grade2 = input("Grade 2: ")
    grade3 = input("Grade 3: ")
    
    with open("exam_grades.txt", "a", encoding="utf-8") as file:
        file.write(f"{first_name} {last_name}: {grade1},{grade2},{grade3},\n")  # Write formatted string


def save_grades():
    with open("exam_grades.txt", "r", encoding="utf-8") as file:
        grade_list = []
        
        for line in file:
            grade_list.append(calculate_grade(line))
            
    with open("results.txt", "w", encoding="utf-8") as file2:
        file2.writelines(grade_list)  # Write the list to the file


while True:
    operation = input("1- Read Grades \n2- Enter Grades \n3- Save Grades \n4- Exit \n")
    
    if operation == "1":
        read_averages()
    elif operation == "2":
        enter_grades()
    elif operation == "3":
        save_grades()
    elif operation == "4":
        break
    else:
        print("Invalid operation, please try again.")
