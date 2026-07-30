name = input("What's your name? ")
age = int(input("What's your age? "))
country = input("What country are you from? ")
favorite_color = input("What's your favorite color ? ")


student = {
    "name": name,
    "age": age,
    "country": country,
    "favorite_color" : favorite_color,
}
def print_student():
  print(f"\nName: {student['name']}")
  print(f"Age: {student['age']}")
  print(f"Country: {student['country']}")
  print(f"Favorite_color: {student['favorite_color']}")
 

new_age = int(input("\nEnter your new age: "))
student["age"] = new_age
print("\nUpdated Student Information")
print_student()
