import random

def generate_number():
    return random.randint(1, 100)


def get_guess():
    return int(input("Your guess: "))


def check_guess(secret, guess):
    if guess == secret:
        print("🎉 Correct!")
        return True

    elif guess < secret:
        print("Too low!")
        return False

    else:
        print("Too high!")
        return False


def play_game():
    secret = generate_number()   # Generate the number ONCE
    attempts = 0

    while True:
        guess = get_guess()
        attempts += 1

        if check_guess(secret, guess):
            print(f"You won in {attempts} attempts!")
            break


play_game()
      
