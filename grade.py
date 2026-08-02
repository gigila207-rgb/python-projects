grades = {
    "Ali": 17,
    "Sara": 19,
    "Adam": 15
}

while True:
    print("""1. Add Student
2. Search Student
3. Update Grade
4. Show All Grades
5. Best Student
6. Exit """)
    choose = int(input("select an operation: "))

    if choose == 1:
        student = input("add the name of the new student: ")
        grade = int(input("add the grade: "))
        grades[student] = grade

    elif choose == 2:
        search_student = input("search for a student: ")
        if search_student in grades:
            print(grades.get(search_student))
        else:
            print("Student not found.")

    elif choose == 3:
        search_student = input("search for a student: ")
        if search_student in grades:
            new_grade = int(input("add the updated grade: "))
            grades[search_student] = new_grade
        else:
            print("Student not found.")

    elif choose == 4:
        for student, grade in grades.items():
            print(f"{student} - {grade}")

    elif choose == 5:
        best_student = None
        best_grade = -1
        for student, grade in grades.items():
            if grade > best_grade:
                best_grade = grade
                best_student = student
        print(f"Best Student: {best_student} ({best_grade})")

    elif choose == 6:
        break





        
    
    
        
        
        
        
    

  
    
