import random

realnumber = random.randint(1, 10)
guess = 0

while guess != realnumber:
    guess = int(input("Select a number between 1 and 10: "))

    if guess < realnumber:
        print("The number is bigger.")

    elif guess > realnumber:
        print("The number is smaller.")

print("🎉 Congratulations! You guessed the correct number!")
