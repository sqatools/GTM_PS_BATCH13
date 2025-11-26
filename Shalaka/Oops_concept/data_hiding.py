class school :
    def __init__(self, name, add, board):
        self.name = name
        self._add = add
        self.__board = board

    def show_school(self):
        print(self.name)

    def _show_add(self):
        print(self._add)

    def __show_board(self):
        print(self.__board)


obj = school("MGM", "Mumbai", "MH")
obj.show_school()
obj._show_add()
obj._school__show_board()
