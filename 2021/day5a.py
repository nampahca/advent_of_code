class Vent:

    def __init__(self, x1, y1, x2, y2):
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2

    @property
    def coords(self):
        return [self._x1, self._y1, self._x2, self._y2]

    def isaxial(self):
        return (self._x1 == self._x2) or (self._y1 == self._y2)


ventlist = []
with open(r"2021\inputs\5.txt", "r") as inp:
    vents = inp.readlines()

for i in vents:
    x1, y1, x2, y2 = i.rstrip('\n\r').replace(" -> ", ",").split(",")
    ventlist.append(Vent(x1, y1, x2, y2))

print(ventlist[0].coords)

for i in range(10):
    print(ventlist[i].isaxial())