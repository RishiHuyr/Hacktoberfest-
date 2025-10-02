import random

def play():
    print("Welcome to Rock, Paper, Scissors!")
    choices = ["rock", "paper", "scissors"]
    while True:
        user = input("Enter rock, paper, scissors or 'quit' to exit: ").lower()
        if user == "quit":
            print("Thanks for playing!")
            break
        if user not in choices:
            print("Invalid choice. Try again.")
            continue
        comp = random.choice(choices)
        print(f"Computer chose: {comp}")

        if user == comp:
            print("It's a tie!")
        elif (user == "rock" and comp == "scissors") or \
             (user == "paper" and comp == "rock") or \
             (user == "scissors" and comp == "paper"):
            print("You win!")
        else:
            print("You lose!")

if __name__ == "__main__":
    play()
