from game_analys import *

game = True
while game:  # 925607913  84 / 104
    hi = 'y'#input("Сыграем? y/n  ")

    if hi == "y":
        cur_numb = NewGame(428459790) # 51 / 62
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
