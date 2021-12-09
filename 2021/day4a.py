import random


class bingoBoard():

    def __init__(self, board):
        self._board = board

    @property
    def board(self):
        return self._board

    def bingo(self):
        lines = [self._board[i] for i in range(len(self._board))] + [list(map(lambda x: x[i], self._board)) for i in range(len(self._board[0]))]
        for line in lines:
            win = 1
            for item in line:
                if not item.endswith("_"):
                    win = 0
            if win:
                break
        return win

    def call(self, number):
        for i, line in enumerate(self._board):
            for j, item in enumerate(line):
                if item == number:
                    self._board[i][j] = item + "_"
        if self.bingo():
            return self.score(number)
        else:
            return 0

    def score(self, called):
        unmarked = 0
        for i in self._board:
            for j in i:
                if "_" not in j:
                    unmarked += int(j)
        return unmarked * int(called)


# lines = [a[j] for j in range(len(a))] + [list(map(lambda x: x[i], a)) for i in range(len(a[0]))]

test = list(map(lambda x: x.split(" "), """24 75 59 41 17
58 74 64 92 39
68  8 78 85 72
18  3 22  4 34
11 76  6 28 50""".splitlines()))

with open(r"2021/inputs/4.txt", "r") as f:
    numbers, *boards = f.readlines()
print(numbers)
numberlist = numbers.split(",")

boardtext = "".join(boards).split("\n\n")
boards = []
for i in boardtext:
    board = []
    for j in filter(lambda x: len(x) >= 2, i.split("\n")):
        line = list(filter(lambda x: x != "", j.split(" ")))
        board.append(line)
    boards.append(bingoBoard(board))

won = 0

for i in numberlist:
    for j in boards:
        a = j.call(i)
        if a:
            print(a)
            won = 1
    if won:
        break
