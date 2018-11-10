import os

def clear():
    os.system('cls')

clear()
while True:

    p1Choice = input("What is your choice player 1? ")
    clear()
    p2Choice = input("What is your choice player 2? ")
    clear()

    if p1Choice == "rock" and p2Choice == "rock" or p1Choice == "paper" and p2Choice == "paper" or p1Choice == "scissor" and p2Choice == "scissor":
        print("It is a tie, what are the chances!!")
    elif p1Choice == "rock" and p2Choice == "scissor":
        print("Player 1 wins! Rock beats scissor")
    elif p1Choice == "rock" and p2Choice == "paper":
        print("Player 2 wins! Paper beats rock")
    elif p1Choice == "paper" and p2Choice == "rock":
        print("Player 1 wins! Paper beats rock")
    elif p1Choice == "paper" and p2Choice == "scissor":
        print("Player 2 wins! Scissor beats paper")
    elif p1Choice == "scissor" and p2Choice == "paper":
        print("Player 1 wins! Scissor beats paper")
    elif p1Choice == "scissor" and p2Choice == "rock":
        print("Player 2 wins! Rock beats paper")    

    choice = input("do you want to play again? y/n ")
    if choice == "y":
        continue
    else:
        break
    

print("Thanks for Playing!!")