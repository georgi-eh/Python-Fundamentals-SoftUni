import random

computer_num = random.randint(1, 100)

while True:
    player_input = input("Guess the number (1-100): ")

    if not player_input.isdigit():
        print("Invalid input. Try again...")
        continue
    else:
        player_num = int(player_input)

    if player_num == computer_num:
        print("You guessed it!")
    elif player_num > computer_num:
        print("Too High!")
    else:
        print("Too Low!")
