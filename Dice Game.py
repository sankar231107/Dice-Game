import random

def roll_dice():
    return random.randint(1, 6)

def play_game():
    player_score = 0
    computer_score = 0

    rounds = int(input("Enter number of rounds: "))

    for i in range(1, rounds + 1):
        print("\nRound", i)

        input("Press Enter to roll dice")

        player_roll = roll_dice()
        computer_roll = roll_dice()

        print("Player rolled:", player_roll)
        print("Computer rolled:", computer_roll)

        if player_roll > computer_roll:
            print("Player wins this round")
            player_score += 1
        elif computer_roll > player_roll:
            print("Computer wins this round")
            computer_score += 1
        else:
            print("This round is a tie")

    print("\nFinal Score")
    print("Player:", player_score)
    print("Computer:", computer_score)

    if player_score > computer_score:
        print("Player wins the game")
    elif computer_score > player_score:
        print("Computer wins the game")
    else:
        print("The game is a draw")

play_game()
