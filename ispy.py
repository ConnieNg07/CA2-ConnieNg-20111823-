# Connie Ng
# 5/12/24
# Python program ispy
import random
import difflib

# List of objects that the game will randomly choose from
objects = ["apple", "banana", "car", "dog", "elephant", "guitar", "house", "tree", "keyboard", "pen"]

# Function to give a hint based on the chosen object
def give_hint(object):
    return f"I spy with my little eye something that starts with '{object[0]}'"

# Function to check if the guessed object is correct
def check_guess(user_guess, object):
    user_guess = user_guess.lower().strip()
    object = object.lower()
    
    # Use difflib to match closely similar words
    match_ratio = difflib.SequenceMatcher(None, user_guess, object).ratio()
    if match_ratio > 0.7:  # If the match is more than 70% similar, consider it correct
        return True
    return False

# Main game function
def play_game():
    # Select a random object from the list
    chosen_object = random.choice(objects)

    print("Welcome to I Spy Game!")
    print("Try to guess the object based on the hints given.")
    
    # Loop until the player guesses the object correctly
    while True:
        hint = give_hint(chosen_object)
        print(hint)

        # Get the user's guess
        user_guess = input("What do you think it is? ").strip()

        # Check if the guess is correct using difflib
        if check_guess(user_guess, chosen_object):
            print("Correct! You guessed it!")
            break
        else:
            print("Oops! Try again!")

# Run the game
if __name__ == "__main__":
    play_game()
