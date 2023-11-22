import colorama
import os


def clear():
    os.system('cls')
colorama.init()

blue_color = colorama.Fore.BLUE
black_color = colorama.Fore.BLACK
cyan_color = colorama.Fore.CYAN
yellow_color = colorama.Fore.YELLOW
green_color = colorama.Fore.GREEN
white_color = colorama.Fore.WHITE
red_color = colorama.Fore.RED


board = list(range(0, 9))
board_size = 3
dashes = 13
spaces = 14
turn_counter = 0
is_win = False
win_coords = (
    (0, 1, 2), (3, 4, 5), (6, 7, 8),
    (0, 3, 6), (2, 5, 8), (1, 4, 7),
    (0, 4, 8), (2, 4, 6)
)
player_token = ''
print(f'{green_color}Tic-tac toe the game for two players. ')

while not is_win:
    for i in range(board_size):
        print(' ' * spaces, end='')
        print('-' * dashes)
        print(' ' * spaces, end='')
        print(f'{blue_color}| {board[0 + i * 3]} |{white_color} {board[1 + i * 3]} |{red_color} {board[2 + i * 3]} |')
        print(' ' * spaces, end='')
        print('-' * dashes)
    if turn_counter % 2 == 0:
        player_token = 'X'
    else:
        player_token = 'O'
    player_answer = input(f'{cyan_color}Where we put a {player_token}?: ')
    try:
        player_answer = int(player_answer)
    except ValueError:
        print(f'{red_color}Неправильный ввод. Нужно ввести число.')
        continue
    try:
        board_value = board[player_answer]
    except IndexError:
        print(f'{red_color}Неправильный ввод. Должны быть числа от 0 до 8 включительно.')
        continue
    if str(board[player_answer]) not in 'XO':
        board[player_answer] = player_token
    else:
        print('This cell is already taken!')
        continue
    clear()
    turn_counter += 1
    if turn_counter > 4:
        for each in win_coords:
            if board[each[0]] == board[each[1]] == board[each[2]]:
                is_win = True
                break
        if is_win:
            for i in range(board_size):
                print(' ' * spaces, end='')
                print('-' * dashes)
                print(' ' * spaces, end='')
                print(f'{green_color}| {board[0 + i * 3]} |{green_color} {board[1 + i * 3]} |{green_color} {board[2 + i * 3]} |')
                print(' ' * spaces, end='')
                print('-' * dashes)
            print(f'{player_token} is win')
            break
    if turn_counter == '9':
        print(f'{green_color}Draw! Your amazing!')
        break
exit_confirmation = input(f'{cyan_color}Нажми Enter для выхода.')
quit()