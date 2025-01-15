import random

def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        return "You win!"
    else:
        return "You lose!"

def main():
    win_streak = 0
    loss_streak = 0

    while True:
        user_choice = input("Choose rock, paper, or scissors (or 'exit' to quit): ").lower()
        
        if user_choice == 'exit':
            print("Thanks for playing!")
            break

        if user_choice not in ["rock", "paper", "scissors"]:
            print("Invalid choice! Please choose rock, paper, or scissors.")
            continue

        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")

        result = determine_winner(user_choice, computer_choice)
        print(result)

        if result == "You win!":
            win_streak += 1
            loss_streak = 0
        elif result == "You lose!":
            loss_streak += 1
            win_streak = 0

        print(f"Current Win Streak: {win_streak}, Current Loss Streak: {loss_streak}\n")

if __name__ == "__main__":
    main()
