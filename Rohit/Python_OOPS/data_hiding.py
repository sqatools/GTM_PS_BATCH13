"""
to achieve the data hiding, we have to define the variable and method name with single or double under score as prefix.
"""
class school():
    def __init__(self, name, address, board):
        self.name = name
        self._address = address
        self.__board = board

    def show_name(self):
        print("School Name :", self.name)

    def _show_school_address(self):
        print("School Address :", self._address)

    def __show_school_board(self):
        print("School board :", self.__board)

obj = school('AITRC','Karad','MH Board')
# when we define any variable/method with single/double underscore as prefix, then
# those variable/method will not show in suggest list.
obj.show_name()

# access variable/method with single underscore as prefix: user can access directly.
obj._show_school_address()

# access variable/method with double underscore as prefix: user has to follow a pattern to access method or variable
# obj._class__variable/method
obj._school__show_school_board()

'''
School Name : AITRC
School Address : Karad
School board : MH Board
'''