import random

def list_int(l):
    num = 0
    for i, v in enumerate(reversed(l)):
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


def outnum(l):
    res = ""
    for i in l:
        res += str(i)
    return res


def reader_numb(path):
    with open(path, 'r') as f:
        lines = f.readlines()[1:-1]
    res = [(int(x[:9]), int(x[23:-1])) for x in lines]
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
        zeroing(number, i)
        sw = i if number.gameList[i - 2] == 0 else i + 1
        for j in range(2, sw):
            zeroing(number, j, 1)


def problemator(number):
    problempos = []
    for i in range(len(number.gameList)):
        if i + 1 == number.gameList[i]: problempos.append(i + 1)
    return problempos




class NewGame:

    def __init__(self, numb, mode=0, old_step=0):
        self.gameList = int_list(numb) if numb != 0 else [random.randint(0, 9) for i in range(9)]
        self.step = 0
        self.old_step = old_step
        self.mode = mode
        self.start = str(outnum(self.gameList))
        if not mode: print("\nТвое число: " + self.start + "\nПозиции:    123456789")

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

    def reshator(self):
        while list_int(self.gameList[1:]) != 0:
            not_problem(self)

            problem = problemator(self)

            if problem:
                for i in range(9):
                    if self.gameList[i] == 0 and i + 1 > problem[0]:
                        for j in range(problem[0]): self.make_move(i + 1, "+")  # print("tut")
                        self.make_move(i + 1, "-")
                        zeroing(self, problem[0])
                    elif self.gameList[i] == 0 and i + 1 < problem[0]:
                        for j in range(problem[0]): self.make_move(i + 1, "-")  # print("tut")
                        self.make_move(i + 1, "+")
                        zeroing(self, problem[0])
                    else:
                        continue
            not_problem(self)

            if list_int(self.gameList[1:]) != 0 and list_int(self.gameList[1:]) > 10:
                for i in self.gameList[1:]:
                    if i == 0:
                        continue
                    else:
                        for j in range(1, i + 1):
                            self.make_move(9, "+")
                self.make_move(9, "-")
            if list_int(self.gameList[1:-1]) == 0 and self.gameList[-1] == 9: self.make_move(2, "-")