import random

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "win"
    else:
        return "lose"

def main():
    user_score = 0
    computer_score = 0
    play_again = True

    print("Welcome to Rock-Paper-Scissors Game!")

    while play_again:
        
        user_choice = input("\nChoose Rock, Paper, or Scissors: ").lower()

        
        if user_choice not in ["rock", "paper", "scissors"]:
            print("Invalid choice! Please choose either Rock, Paper, or Scissors.")
            continue

        
        choices = ["rock", "paper", "scissors"]
        computer_choice = random.choice(choices)

        
        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")

        
        result = determine_winner(user_choice, computer_choice)

        
        if result == "win":
            print("You win this round!")
            user_score += 1
        elif result == "lose":
            print("You lose this round.")
            computer_score += 1
        else:
            print("It's a tie!")

        print(f"\nCurrent Score: You {user_score} - Computer {computer_score}")

        
        play_again_input = input("\nDo you want to play again? (y/n): ").lower()
        if play_again_input != 'y':
            play_again = False

    print("\nFinal Score:")
    print(f"You: {user_score}")
    print(f"Computer: {computer_score}")
    print("Thanks for playing!")

if __name__ == "__main__":
    main()
