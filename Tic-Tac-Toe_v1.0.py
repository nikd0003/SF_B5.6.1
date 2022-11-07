from os import system, name
from time import sleep
# from random import randint


def clear():    # clear display
    if name == 'nt':    # for windows
        _ = system('cls')
    else:    # for mac and linux(here, os.name is 'posix')
        _ = system('clear')


def draw_board(board):    # drowing board
    clear()
    print(f"   0  1  2")
    for i in range(3):
        print(f"{i}  {board[0 + i * 3]}  {board[1 + i * 3]}  {board[2 + i * 3]}")


def take_input(player_token):    #
    valid = False
    while not valid:
        player_answer = input(f"""Вводите координаты через \' \' или \',\'. Первая цифра - строка, вторая - столбец.
Например: \'0 2\' или \'1,0\' или \'2, 1\' или \'00\' (вводите без кавычек)
Куда поставим {player_token} ? """)
        player_answer = player_answer.replace(',', '')
        player_answer = player_answer.replace(' ', '')
        length_player_answer = len(player_answer)
#        if 3 <= length_player_answer <=1:
#            print(f"Координаты состоят из двух цифр!")
        if player_answer in dict_coord:
            player_answer = dict_coord[player_answer]
        else:
            print("Этот неверные координаты!")
        try:
            player_answer = int(player_answer)
        except:
            print("Некорректный ввод. Вы уверены, что ввели число?")
            continue
        if 0 <= player_answer <= 8 and length_player_answer == 2:
            if(str(board[player_answer]) not in "XO"):
                board[player_answer] = player_token
                valid = True
            else:
                print("===> Эта клетка уже занята! <===")
        else:
            print("Некорректный ввод. Вводите цифры 0, 1 или 2.")


def check_win(board):
    win_coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for each in win_coord:
        if board[each[0]] == board[each[1]] == board[each[2]] != "-":
            if board[each[0]] == board[each[1]] == board[each[2]]:
                return board[each[0]]
    return False


def main(board):
    counter = 0
    win = False
    while not win:
        draw_board(board)
        if counter % 2 == 0:
            take_input("X")
        else:
            take_input("O")
        counter += 1
        if counter > 4:
            tmp = check_win(board)
            if tmp:
                draw_board(board)
                print("\n")
                print(f"*" * 29, f"\n***   {tmp}! {tmp}! {tmp}!  выиграл!  ***")
                print(f"*" * 29)
                win = True
                return
        if counter == 9:
            draw_board(board)
            print("\nБыло трудно и мы почти победили, но пока ничья!")
            return
    draw_board(board)


if __name__ == "__main__":
    y = 0
    dict_coord = dict.fromkeys(['00', '01', '02', '10', '11', '12', '20', '21', '22'])
    for x in dict_coord:
        dict_coord[x] = y
        y += 1
    board = list("-" * 9)
    clear()
    print(f"*" * 41, f"\n* Игра Крестики-нолики для двух игроков *")
    print(f"*" * 41)
    FirstPlayer = input("Первый игрок, представьтесь как Вас зовут: ")
    SecondPlayer = input("Второй игрок, представьтесь как Вас зовут: ")
    print("\n")
    print(f"*" * 36)
    print(f"****  Добро пожаловать в игру!  ****")
    print(f"*" * 36)
    sleep(2)
    main(board)
    input("\nНажмите Enter для выхода.")