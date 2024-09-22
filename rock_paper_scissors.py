import random

while True:
    rock = 'Rock'
    paper = 'Paper'
    scissors = 'Scissors'

    player_move = input('Choose [r]ock, [p]aper, [s]isscors: ')

    if player_move == 'r':
        player_move = rock
    elif player_move == 'p':
        player_move = paper
    elif player_move == 's':
        player_move = scissors
    else:
        again = input("Invalid input. Try again? Y/N ")
        if again.lower() == 'y':
            print()
            continue
        else:
            print('Thank you for playing!')
            break

    computer_choice = random.randint(1, 3)

    computer_move = ""

    if computer_choice == 1:
        computer_move = rock
    elif computer_choice == 2:
        computer_move = paper
    else:
        computer_move = scissors

    print(f'The computer chose {computer_move}.')

    if (player_move == rock and computer_move == scissors) or \
            (player_move == scissors and computer_move == paper) or \
            (player_move == paper and computer_move == rock):
        print('You win!')
    elif computer_move == player_move:
        print('Draw!')
    else:
        print('You lose!')

    restart = input('Play again? Y/N ')

    if restart.lower() == 'y':
        print()
        continue
    else:
        print('Thank you for playing!')
        break
