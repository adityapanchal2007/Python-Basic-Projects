import random

items = ["rock", "paper", "scissors"]
computer_choice = random.choice(items)

user_choice = input("Enter your choice: ").lower()

 # User wins
if user_choice == computer_choice:
    print("Match Draw..!")

elif user_choice == "rock" and computer_choice == "scissors":
    print("Hurray !\n You Beat the Computer..!\n")

elif user_choice == "paper" and computer_choice == "rock":
    print("Hurray !\n You Beat the Computer..!\n")

elif user_choice == "scissors" and computer_choice == "paper":
    print("Hurray !\n You Beat the Computer..!\n")

# Computer wins

elif computer_choice == "paper" and user_choice == "rock":
    print("Oops!\n Computer wins..!, Better Luck Next Time..!! \n")

elif computer_choice == "scissors" and user_choice == "paper":
    print("Oops!\n Computer wins..!, Better Luck Next Time..!! \n")

elif computer_choice == "rock" and user_choice == "scissors":
    print("Oops!\n Computer wins..!, Better Luck Next Time..!! \n")

elif user_choice not in items:
    print("Invalid choice..! Please choose from:-> rock, paper, scissors.")

else:
    print("Game Over....!!")

restart = input("Do you want to play again? (yes/no): \n").lower()
if restart == "yes":
    exec(open("rock_paper_scissors_game.py").read())
else:
    print("Thanks for playing..!!")