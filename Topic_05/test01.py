import random

options = ["stone", "scissor", "paper"]

PlayerAnswer = input("Enter stone, scissor or paper: ")
computer = random.choice(options)

if PlayerAnswer not in options:
    print("Wrong operation")
else:
    print("Computer:", computer)

if PlayerAnswer == computer:
    print("Draw")
elif (PlayerAnswer == "stone" and computer == "scissor") or (PlayerAnswer == "scissor" and computer == "paper") or (PlayerAnswer == "paper" and computer == "stone"):
    print("You win")
else:
    print("Computer wins")