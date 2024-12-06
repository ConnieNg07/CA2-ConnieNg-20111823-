# Connie Ng
# 3/12/24
# Program a Coin Toss 
import random

# Function to simulate the coin toss
def coin_toss():
    return random.choice(['Heads', 'Tails'])

# Function to play the coin toss game
def play_game():
    print("Welcome to the Coin Toss Game!")
    
    while True:
        user_choice = input("Choose Heads or Tails: ").strip().lower()
        
        # Validate the user's choice
        if user_choice not in ['heads', 'tails']:
            print("Invalid choice! Please choose either 'Heads' or 'Tails'.")
            continue
        
        # Simulate the toss
        toss_result = coin_toss()
        print(f"The coin landed on: {toss_result}")
        
        # Check if the user's guess is correct
        if user_choice == toss_result.lower():
            print("Congratulations! You guessed correctly.")
        else:
            print("Oops! You guessed wrong.")
        
        # Ask if the user wants to play again
        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again != 'yes':
            print("Thanks for playing! Goodbye!")
            break

# Start the game
if __name__ == "__main__":
    play_game()
