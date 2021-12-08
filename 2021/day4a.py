import random


class bingoBoard():

    def __init__(self, board):
        self._board = board

    @property
    def board(self):
        print(self._board)

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
        print(self._board)


# lines = [a[j] for j in range(len(a))] + [list(map(lambda x: x[i], a)) for i in range(len(a[0]))]

test = list(map(lambda x: x.split(" "), """24 75 59 41 17
58 74 64 92 39
68  8 78 85 72
18  3 22  4 34
11 76  6 28 50""".splitlines()))

with open(r"2021/inputs/4.txt", "r") as f:
    numbers, *boards = f.readlines()
print(numbers)
boardtext = "".join(boards).split("\n\n")
boards = []
for i in boardtext:
    board = []
    for j in i.split("\n"):
]
    boards.append(bingoBoard(list(filter(lambda x: x != "", i.split("\n")))))

print(boards[0].board)

print(boards)
print(test)
a = bingoBoard(test)

a.call("58")
a.call("24")
a.call("68")
a.call("18")
print(a.bingo())
a.call("11")
print(a.bingo())
