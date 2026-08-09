import json

# Initial student data
student = {
    "name": "Ali",
    "age": 16,
    "grades": [15, 17, 19]
}

# 1️⃣ Save the student to student.json
with open("student.json", "w") as f:
    json.dump(student, f)

# 2️⃣ Load the student from the file
with open("student.json", "r") as f:
    student = json.load(f)

# 3️⃣ Change the age
student["age"] = student["age"] + 1

# 4️⃣ Add a new grade
student["grades"].append(20)

# 5️⃣ Save the updated student
with open("student.json", "w") as f:
    json.dump(student, f, indent=4)

# 6️⃣ Load it one more time and print it
with open("student.json", "r") as f:
    student = json.load(f)

print(student)

