
class CustomList(list):
    def _getitem_(self, index):
        if index <= 0:
            raise ValueError("index out of bound")
        return super()._getitem_(index-1)

    def _setitem_(self, index, value):
        if index <= 0:
            raise ValueError("index out of bound")
        return super()._setitem_(index-1, value)



l = CustomList()
l.append(1)
l.append(2)
l.append(3)
l.append(4)
l.append(7)
l.append(8)
l.append(5)
print(l)

l[1] = 56
l[2] = 45
l[3] = 87
l[4] = 96
print(l)
print(l[3])
