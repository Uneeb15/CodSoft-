import random

def get_computer_choice():
    """Randomly select rock, paper, or scissors for the computer."""
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    """Determine the winner based on user's and computer's choice."""
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "user"
    else:
        return "computer"

def display_result(user_choice, computer_choice, winner):
    """Display the result of the round."""
    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    if winner == "tie":
        print("It's a tie!")
    elif winner == "user":
        print("You win!")
    else:
        print("Computer wins!")

def play_game():
    user_score = 0
    computer_score = 0

    while True:
        # User input
        user_choice = input("\nChoose rock, paper, or scissors (or type 'quit' to stop playing): ").lower()
        if user_choice == "quit":
            break

        # Validate input
        if user_choice not in ["rock", "paper", "scissors"]:
            print("Invalid input! Please choose rock, paper, or scissors.")
            continue

        # Computer choice
        computer_choice = get_computer_choice()

        # Determine winner
        winner = determine_winner(user_choice, computer_choice)

        # Display result
        display_result(user_choice, computer_choice, winner)

        # Update scores
        if winner == "user":
            user_score += 1
        elif winner == "computer":
            computer_score += 1

        # Display score
        print(f"\nScore - You: {user_score} | Computer: {computer_score}")

        # Ask to play again
        play_again = input("\nDo you want to play another round? (yes/no): ").lower()
        if play_again != "yes":
            print("\nThanks for playing!")
            break

# Start the game
play_game()
