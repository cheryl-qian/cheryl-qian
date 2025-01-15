import random

def get_user_choice():
    user_input = input("Choose Rock, Paper, or Scissors: ").lower()
    while user_input not in ["rock", "paper", "scissors"]:
        print("Invalid choice! Please try again.")
        user_input = input("Choose Rock, Paper, or Scissors: ").lower()
    return user_input

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    total_wins = 0
    total_losses = 0
    current_win_streak = 0
    current_loss_streak = 0

    print("Welcome to Rock-Paper-Scissors!")
    
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        
        print(f"You chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")
        
        result = determine_winner(user_choice, computer_choice)
        print(result)

        # Update win/loss counts and streaks
        if result == "You win!":
            total_wins += 1
            current_win_streak += 1
            current_loss_streak = 0  # Reset loss streak
        elif result == "Computer wins!":
            total_losses += 1
            current_loss_streak += 1
            current_win_streak = 0  # Reset win streak

        # Display the stats
        print(f"Total Wins: {total_wins}, Total Losses: {total_losses}")
        print(f"Current Win Streak: {current_win_streak}, Current Loss Streak: {current_loss_streak}")

        # Ask if the user wants to play again
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            break

    print("Thank you for playing!")

if __name__ == "__main__":
    play_game()

