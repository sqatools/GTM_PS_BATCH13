class school:
    def __init__(self, name, address, board):
        self.name = name
        self._address = address
        self.__board = board


    def show_name(self):
        print("School name :", self.name)


    def _show_school_address(self):
        print("School Address :", self._address)

    def __show_board_name(self):
        print("School board name :", self.__board)