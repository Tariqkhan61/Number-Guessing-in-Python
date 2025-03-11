# Guess the Number Game By Computer
import random

def guess_the_number():
    number = random.randint(1, 100)  # Fixed typo: radiant -> randint
    guesses_left = 7  # Fixed typo: guess_left -> guesses_left

    # Welcome Message
    print("Welcome to the Number Guessing Game")
    print("I am thinking of a number between 1 to 100")

    # Now we generate while loop
    while guesses_left > 0:
        print(f"\nYou have {guesses_left} guesses left.")
        try:
            guess = int(input("Take a guess: "))
        except ValueError:
            print("Invalid Input: Please enter a number")
            continue

        # Now guess the secret number
        if guess < number:
            print("Too low. Try again!")
        elif guess > number:
            print("Too high. Try again!")
        else:
            print(f"Congratulations! You guessed the correct number in {7 - guesses_left + 1} tries.")
            return

        guesses_left -= 1

    print(f"\nYou ran out of guesses. The number was {number}.")
    guess_the_number()

guess_the_number()
