# Connie Ng
# 25/11/24
# Word Jumble using randomisation and string manipulation
import random

# List of words to choose from
word_list = ['Distinguishability', 'Python', 'Pink', 'Programming', 'Minecraft', 'Computer', 'Spotify', 'Logistical']

# Function to scramble a word
def scramble_word(word):
    word_list = list(word)  # Convert the word into a list of characters
    random.shuffle(word_list)  # Shuffle the list of characters
    return ''.join(word_list)  # Join the characters back into a string

# Main function for the game
def play_game():
    # Choose a random word from the list
    word_to_guess = random.choice(word_list)
    
    # Scramble the word
    jumbled_word = scramble_word(word_to_guess)
    
    print("Welcome to the Word Jumble Game!")
    print(f"Here is the jumbled word: {jumbled_word}")
    
    # Allow the player to guess
    guess = input("Guess the original word: ").lower()
    
    # Check if the guess is correct (case-insensitive comparison)
    if guess == word_to_guess.lower():
        print("Congratulations! You guessed the word correctly.")
    else:
        print(f"Oops! The correct word was {word_to_guess}.")

    # Ask if the user wants to play again
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == 'yes':
        play_game()
    else:
        print("Thanks for playing! Goodbye.")

# Start the game
play_game()
