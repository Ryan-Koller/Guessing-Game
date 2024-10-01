import random  # Import the random module to generate random numbers

def get_guess():
    """Function to get a valid guess from the user."""
    while True:  # Keep asking until a valid guess is received
        try:
            # Ask the user to input a number and convert it to an integer
            guess = int(input("Guess a number between 1 and 100: "))
            # Check if the guess is within the valid range
            if 1 <= guess <= 100:
                return guess  # Return the valid guess
            else:
                print("Please guess a number within the range!")  # Prompt if out of range
        except ValueError:
            print("That's not a valid number. Please enter a number.")  # Handle non-integer inputs

def play_game(user_name):
    """Main function to play the guessing game."""
    number_to_guess = random.randint(1, 100)  # Generate a random number between 1 and 100
    attempts = 0  # Initialize attempts counter
    max_attempts = 5  # Set maximum allowed attempts

    # Loop until the user runs out of attempts
    while attempts < max_attempts:
        guess = get_guess()  # Get a valid guess from the user
        attempts += 1  # Increment the attempts counter

        # Check if the guess is too low, too high, or correct
        if guess < number_to_guess:
            print("Too low! Try again.")
        elif guess > number_to_guess:
            print("Too high! Try again.")
        else:
            # User has guessed correctly
            print(f"Congratulations, {user_name}! You've guessed the number {number_to_guess} in {attempts} attempts.")
            return True, attempts  # Return success and attempts used

    # If the user runs out of attempts, reveal the correct number
    print(f"Sorry, {user_name}. You've run out of attempts! The number was {number_to_guess}.")
    return False, attempts  # Return failure and attempts used

def main():
    """Main function to run the game loop and manage user scores."""
    leaderboard = {}  # Dictionary to keep track of user scores

    print("Welcome to the Number Guessing Game!")  # Welcome message
    user_name = input("Please enter your name: ")  # Get the user's name

    while True:  # Loop to allow multiple games
        win, attempts = play_game(user_name)  # Play a game and capture win status and attempts

        # Initialize user's record if it's their first game
        if user_name not in leaderboard:
            leaderboard[user_name] = {'wins': 0, 'losses': 0, 'least_attempts': float('inf')}
        
        # Update leaderboard based on win/loss
        if win:
            leaderboard[user_name]['wins'] += 1  # Increment wins
            leaderboard[user_name]['least_attempts'] = min(leaderboard[user_name]['least_attempts'], attempts)  # Update least attempts
        else:
            leaderboard[user_name]['losses'] += 1  # Increment losses

        # Display user's current leaderboard stats
        print(f"Leaderboard for {user_name}: Wins: {leaderboard[user_name]['wins']}, Losses: {leaderboard[user_name]['losses']}, Least Attempts: {leaderboard[user_name]['least_attempts'] if leaderboard[user_name]['least_attempts'] != float('inf') else 'N/A'}")
        
        # Ask if the user wants to play again
        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again != 'yes':  # Exit if the user doesn't want to play again
            print("Thanks for playing! Here’s your final record:")
            print(f"Wins: {leaderboard[user_name]['wins']}, Losses: {leaderboard[user_name]['losses']}, Least Attempts: {leaderboard[user_name]['least_attempts'] if leaderboard[user_name]['least_attempts'] != float('inf') else 'N/A'}")
            break  # End the game loop

# Entry point of the program
if __name__ == "__main__":
    main()  # Call the main function to start the game
