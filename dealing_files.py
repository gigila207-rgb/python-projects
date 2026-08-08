with open("students.txt", "r") as file:
    for line in file:
        student = line.strip()

        if len(student) > 3:
            print(student)
