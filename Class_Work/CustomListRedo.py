class CustomList(list):
    def __getitem__(self, index):
        if index <=0:
            raise ValueError("index of out of bound")
        super().__getitem__(index-1)


    def __setitem__(self, value, index):
        if index <= 0:
            raise ValueError("index out of bound")
        super().__setitem__(index-1, value)


l=CustomList()
l.append(1)
l.append(2)
l.append(3)
l.append(5)
print(l)