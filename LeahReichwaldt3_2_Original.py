import random


def run_game():
    user_choice = input('Enter response: ').strip().lower()
    while True:
        if user_choice.lower() not in ('rock', 'paper', 'scissor', 'scissors'):
            user_choice = input('Enter valid response: ')
        else:
            break
    random_num = random.randint(1, 4)
    outcome = 0
    computer_choice = ''

    if random_num == 1:
        computer_choice = 'rock'
    elif random_num == 2:
        computer_choice = 'paper'
    else:
        computer_choice = 'scissor'

    if user_choice == computer_choice:
        print(f'HAL is {computer_choice}. You are {user_choice}. You tie.')
        outcome = 0
    elif user_choice == 'rock':
        if computer_choice == 'scissor':
            print(f'HAL is {computer_choice}. You are {user_choice}. You win.')
            outcome = 1
        else:
            print(f'HAL is {computer_choice}. You are {user_choice}. You lose.')
            outcome = -1
    elif user_choice == 'paper':
        if computer_choice == 'rock':
            print(f'HAL is {computer_choice}. You are {user_choice}. You win.')
            outcome = 1
        else:
            print(f'HAL is {computer_choice}. You are {user_choice}. You lose.')
            outcome = -1
    elif user_choice == 'scissor' or 'scissors':
        if computer_choice == 'paper':
            print(f'HAL is {computer_choice}. You are {user_choice}. You win.')
            outcome = 1
        else:
            print(f'HAL is {computer_choice}. You are {user_choice}. You lose.')
            outcome = -1

    return outcome


def main():
    random.seed(1)
    print('----------------------')
    print('Rock - Paper - Scissor')
    print('----------------------')

    game_counter = 0
    final_score = 0

    while game_counter < 3:
        game_counter += 1
        final_score = final_score + run_game()
        if final_score == 2 or final_score == -2:
            break

    if final_score < 0:
        print("GAME OVER - HAL WINS")
    elif final_score == 0:
        print("GAME OVER - IT'S A TIE")
    elif final_score > 0:
        print("GAME OVER - YOU WIN")


if __name__ == '__main__':
    main()
