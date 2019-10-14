import random
import os
import sys


def list_int(L):
    num = 0
    for i, v in enumerate(reversed(L)):
        num += v * 10 ** i
    return num


def int_list(x):
    res = []
    while x > 0:
        res.append(x % 10)
        x //= 10
    while len(res) < 9:
        res.append(0)
    res.reverse()
    return res


def outnum(L):
    res = ""
    for i in L:
        res += str(i)
    return res


def reader_numb(path):
    res = [(int(x[7:16]), int(x[24:-1])) for x in open(path).readlines()]
    return res


def zeroing(number, pos, q=0):
    flag = number.gameList[pos - 1]
    while number.gameList[pos - 1] != 0 or number.gameList[pos - 1] == pos:
        if number.gameList[pos - 1] > pos:
            number.make_move(pos, "+")
        elif number.gameList[pos - 1] < pos:
            number.make_move(pos, "-")
        else:
            break
    if flag != 1 and q != 0:
        rep = pos if number.gameList[pos - 2] == 0 else pos + 1
        for j in range(2, rep):
            zeroing(number, j)


def not_problem(number):
    for i in range(2, 10):
        zeroing(number, i);
        sw = i if number.gameList[i - 2] == 0 else i + 1
        for j in range(2, sw):
            zeroing(number, j, 1)


def problemator(number):
    problempos = []
    for i in range(len(number.gameList)):
        if i + 1 == number.gameList[i]: problempos.append(i + 1)
    return problempos


def reshator(number):
    while list_int(number.gameList[1:]) != 0:
        not_problem(number)

        problem = problemator(number)

        if problem:
            for i in range(9):
                if number.gameList[i] == 0 and i + 1 > problem[0]:
                    for j in range(problem[0]): number.make_move(i + 1, "+")  # print("tut")
                    number.make_move(i + 1, "-")
                    zeroing(number, problem[0])
                elif number.gameList[i] == 0 and i + 1 < problem[0]:
                    for j in range(problem[0]): number.make_move(i + 1, "-")  # print("tut")
                    number.make_move(i + 1, "+")
                    zeroing(number, problem[0])
                else:
                    continue
        not_problem(number)

        if list_int(number.gameList[1:]) != 0 and list_int(number.gameList[1:]) > 10:
            for i in number.gameList[1:]:
                if i == 0:
                    continue
                else:
                    for j in range(1, i + 1):
                        number.make_move(9, "+")
            number.make_move(9, "-")
        if list_int(number.gameList[1:-1]) == 0 and number.gameList[-1] == 9: number.make_move(2, "-")

class NewGame:

    def __init__(self, numb, mode=0):
        self.gameList = int_list(numb) if numb != 0 else [random.randint(0, 9) for i in range(9)]
        self.step = 0
        self.mode = mode
        if not mode: print("\nТвое число: " + str(outnum(self.gameList)) + "\nПозиции:    123456789")

    def make_move(self, pos, sign):
        pos = int(pos)

        if sign == "+":
            if self.gameList[pos - 1] - 1 == -1:
                self.gameList[pos - 1] = self.gameList[pos - 1] + 1 if self.gameList[pos - 1] != 9 else 0
            else:
                self.gameList[self.gameList[pos - 1] - 1] = self.gameList[self.gameList[pos - 1] - 1] - 1 if \
                    self.gameList[self.gameList[pos - 1] - 1] != 0 else 9
                self.gameList[pos - 1] = self.gameList[pos - 1] + 1 if self.gameList[pos - 1] != 9 else 0

        elif sign == "-":
            if self.gameList[pos - 1] - 1 == -1:
                self.gameList[pos - 1] = self.gameList[pos - 1] - 1 if self.gameList[pos - 1] != 0 else 9
            else:
                self.gameList[self.gameList[pos - 1] - 1] = self.gameList[self.gameList[pos - 1] - 1] + 1 if \
                    self.gameList[self.gameList[pos - 1] - 1] != 9 else 0
                self.gameList[pos - 1] = self.gameList[pos - 1] - 1 if self.gameList[pos - 1] != 0 else 9
        self.step += 1
        if not self.mode:
            print("\nТвое число: " + outnum(self.gameList) + " " + str(pos), sign,
                  str(self.step) + "\nПозиции:    123456789")
