import random
import guessing_art

number_to_guess = random.randint(1, 101)

print(guessing_art.logo)
print("Welcome to the Number Guessing Game!")
level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

if level == 'easy':
    attempts = 10
elif level == 'hard':
    attempts = 5
else:
    attempts = 0

guessed_correctly = False

while attempts > 0 and not guessed_correctly:
    print(f"You have {attempts} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))

    if guess < number_to_guess:
        print("Too low.")
    elif guess > number_to_guess:
        print("Too high.")
    else:
        print(f"You got it! The answer was {number_to_guess}.")
        guessed_correctly = True

    attempts -= 1

if not guessed_correctly:
    print(f"You've run out of guesses. You lose. The number was {number_to_guess}.")
