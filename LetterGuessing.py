# Connie Ng
# 4/12/24
# Letter Guessing Game
import random
import string
import difflib

def letter_guessing_game():
    # Generate a random letter from the alphabet
    letter_to_guess = random.choice(string.ascii_lowercase)
    
    print("Welcome to the Letter Guessing Game!")
    print("I have selected a letter from 'a' to 'z'. Try to guess it!")

    while True:
        # Prompt user for their guess
        user_guess = input("Enter your guess: ").lower()

        # Check if the guess is valid (only one letter and alphabetic)
        if len(user_guess) != 1 or user_guess not in string.ascii_lowercase:
            print("Invalid input! Please enter a single letter from 'a' to 'z'.")
            continue

        # Check if the guess is correct
        if user_guess == letter_to_guess:
            print("Congratulations! You guessed the letter correctly.")
            break
        else:
            # Provide feedback using difflib to show similarity
            closest_matches = difflib.get_close_matches(user_guess, string.ascii_lowercase, n=1, cutoff=0.5)
            if closest_matches:
                print(f"Oops! The letter is not '{user_guess}'. Maybe you meant '{closest_matches[0]}'?")
            else:
                print("Oops! Your guess is way off. Try again!")

if __name__ == "__main__":
    letter_guessing_game()
