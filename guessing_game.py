import random

def main():
    high_score = float('inf')  # Initialize high score to infinity
    while True:
        print("Welcome to the Number Guessing Game!")
        number_to_guess = random.randint(1, 100)
        attempts = 0

        while True:
            try:
                guess = int(input("Guess a number between 1 and 100: "))
                attempts += 1

                if guess < 1 or guess > 100:
                    print("Please guess a number within the range!")
                    continue

                if guess < number_to_guess:
                    print("Too low! Try again.")
                elif guess > number_to_guess:
                    print("Too high! Try again.")
                else:
                    print(f"Congratulations! You've guessed the number {number_to_guess} in {attempts} attempts.")
                    if attempts < high_score:
                        high_score = attempts
                        print(f"New high score: {high_score} attempts!")
                    break
            except ValueError:
                print("That's not a valid number. Please enter a number.")

        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again != 'yes':
            print("Thanks for playing! Your best score was: {}".format(high_score if high_score != float('inf') else "N/A"))
            break

if __name__ == "__main__":
    main()
