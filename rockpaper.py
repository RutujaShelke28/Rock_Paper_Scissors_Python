import random
from colorama import init, Fore, Style
import time

init()

while True:  

    print(Fore.LIGHTYELLOW_EX + """ Let's start the game. Let me explain the Rules:  
1) Rule 1: If player opts Rock and comp opts paper then comp wins or Vice versa.  
2) Rule 2: If player opts Paper and comp opts scissors then comp wins or vice versa.
3) Rule 3: If player opts Scissors and comp opts Rock then comp wins or vice versa. 
4) Rule 4: else Tie""" + Style.RESET_ALL)

    options = ["rock", "paper", "scissors"]

    # Player's Turn
    player_score = 0
    computer_score = 0

    rounds = int(input("Enter the number of rounds you want to play: "))
    current_round = 1

    while current_round <= rounds:
        try:
            player_choice = int(input("Enter your choice (0 for rock / 1 for paper / 2 for scissors): "))
            if player_choice not in [0, 1, 2]:
                print("Oops!! Incorrect, Please enter a valid choice")
                continue
        except ValueError:
            print("Please enter a number only.")
            continue

        print("You choose:", options[player_choice])

        # Computer's Turn
        comp_choice = random.randint(0, 2)

        print("Rock...")
        time.sleep(1)
        print("Paper...")
        time.sleep(1)
        print("Scissors...")
        time.sleep(1)
        print("Shoot!!")
        time.sleep(1)

        print("Computer choose:", options[comp_choice])
        time.sleep(1)

        # Game's Rule
        if (player_choice == 0 and comp_choice == 1) or \
           (player_choice == 1 and comp_choice == 2) or \
           (player_choice == 2 and comp_choice == 0):
            print(Fore.RED + "Computer Wins!" + Style.RESET_ALL)
            computer_score += 1
        elif (player_choice == 0 and comp_choice == 2) or \
             (player_choice == 1 and comp_choice == 0) or \
             (player_choice == 2 and comp_choice == 1):
            print(Fore.GREEN + "Player Wins!" + Style.RESET_ALL)
            player_score += 1
        else:
            print(Fore.YELLOW + "It's a Tie!" + Style.RESET_ALL)

        current_round += 1

    print("\n--- Final Result ---")
    if computer_score > player_score:
        print("Computer Won the Game!!")
    elif player_score > computer_score:
        print("Player Won the Game!!")
    else:
        print("It's a Tie Overall!!")

    ans = input("\nDo you want to play again? (y/n): ").lower()
    if ans != 'y':
        print("Thanks for playing!!")
        break