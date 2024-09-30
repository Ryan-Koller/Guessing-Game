import random

def get_guess():
    while True:
        try:
            guess = int(input("Guess a number between 1 and 100: "))
            if 1 <= guess <= 100:
                return guess
            else:
                print("Please guess a number within the range!")
        except ValueError:
            print("That's not a valid number. Please enter a number.")

def play_game(user_name):
    number_to_guess = random.randint(1, 100)
    attempts = 0
    max_attempts = 5

    while attempts < max_attempts:
        guess = get_guess()
        attempts += 1

        if guess < number_to_guess:
            print("Too low! Try again.")
        elif guess > number_to_guess:
            print("Too high! Try again.")
        else:
            print(f"Congratulations, {user_name}! You've guessed the number {number_to_guess} in {attempts} attempts.")
            return True, attempts

    print(f"Sorry, {user_name}. You've run out of attempts! The number was {number_to_guess}.")
    return False, attempts

def main():
    leaderboard = {}
    
    print("Welcome to the Number Guessing Game!")
    user_name = input("Please enter your name: ")

    while True:
        win, attempts = play_game(user_name)

        if user_name not in leaderboard:
            leaderboard[user_name] = {'wins': 0, 'losses': 0, 'least_attempts': float('inf')}
        
        if win:
            leaderboard[user_name]['wins'] += 1
            leaderboard[user_name]['least_attempts'] = min(leaderboard[user_name]['least_attempts'], attempts)
        else:
            leaderboard[user_name]['losses'] += 1

        print(f"Leaderboard for {user_name}: Wins: {leaderboard[user_name]['wins']}, Losses: {leaderboard[user_name]['losses']}, Least Attempts: {leaderboard[user_name]['least_attempts'] if leaderboard[user_name]['least_attempts'] != float('inf') else 'N/A'}")
        
        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again != 'yes':
            print("Thanks for playing! Here’s your final record:")
            print(f"Wins: {leaderboard[user_name]['wins']}, Losses: {leaderboard[user_name]['losses']}, Least Attempts: {leaderboard[user_name]['least_attempts'] if leaderboard[user_name]['least_attempts'] != float('inf') else 'N/A'}")
            break

if __name__ == "__main__":
    main()
