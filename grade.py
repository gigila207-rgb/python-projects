grades = {
    "Ali": 17,
    "Sara": 19,
    "Adam": 15
}
print("""1. Add Student
2. Search Student
3. Update Grade
4. Show All Grades
5. Best Student
6. Exit """)
while True:
  choose =int(input("select an operation :"))
    if choose == 1:
        student = input("add the name of the new student : ")
        grade = input("add the the grade : ")
        grades[student] = grade 

    elif choose == 2:
        search_student = input("search for a student: ")
        if search_student in grades:
            print(grades.get( search_student ))
        else:
            print("Contact not found.")
    elif choose == 3:
        search_student = input("search for a student: ")
        new_grade = input("add the updated grade  : ")
        grades[search_student] = new_grade 
        
     elif choose == 4:
        
    
    
        
        
        
        
    

  
    
