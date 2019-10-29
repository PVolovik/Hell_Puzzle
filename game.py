from game_analys import *

game = True
while game:  # 925607913  84 / 104
    hi = input("Сыграем? y/n  ")

    if hi == "y":
        cur_numb = NewGame(925607913)
        gameList = cur_numb.gameList

        flag = True if list_int(gameList) != 123456789 else False
        while flag:
            vvod = input("Делай ход: ")
            move = tuple(vvod)

            if vvod == "lan":
                print("Сдался? Слабак!")
                break
            elif vvod == "lol":
                cur_numb.reshator()
                if gameList[0] == 0:
                    print("Поздравляю, ты выйграл! Шагов %s" % cur_numb.step)
                    flag = False
                    continue
                elif gameList[0] != 1:
                    for i in range(gameList[0], 10):  # когда не 0 только первый
                        cur_numb.make_move(i, "+")
                        cur_numb.make_move(i, "-")
                else:
                    for i in range(9):  # когда первый 1
                        cur_numb.make_move(2, "+")
                        cur_numb.make_move(2, "-")

            elif len(move) != 2 or not move[0].isdigit():
                print("Неправильно ты ходишь: вводи n+ или n-, n=1..9")
                continue

            else:
                cur_numb.make_move(*move)

            if list_int(gameList) == 0:
                print("Поздравляю, ты выйграл! Шагов %s" % cur_numb.step)
                #print(new_numb.gameList)
                flag = False
            elif list_int(gameList) == 123456789:
                print("Поздравляю, ты проиграл! Шагов %s" % cur_numb.step)
                flag = False
    # else: print("Пока")
    elif hi == "n":
        print("Пока")
        game = False
    else:
        print("Не понял ввод, повтори")
