import random

# Randomly generate a number between 0 and 20
magic_number = random.randint(0, 20)
max_attempts = 5  # limit number of guesses

print("Welcome to the Magic Number Guessing Game!")
print("I have chosen a number between 0 and 20. Can you guess it?")
print(f"You have {max_attempts} attempts.")

attempts = 0

while attempts < max_attempts:
    user_input = input("Enter your guess: ")

    # Input validation
    if not user_input.isdigit():
        print("Please enter a valid integer!")
        continue

    guess = int(user_input)
    attempts += 1

    # Check the guess
    if guess == magic_number:
        print(f"Congratulations! You guessed the magic number {magic_number} in {attempts} attempts!")
        break
    elif guess < magic_number:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")

if guess != magic_number:
    print(f"Sorry! You've used all {max_attempts} attempts. The magic number was {magic_number}.")