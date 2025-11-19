from class_file1 import school

# obj = school("Shishukunj International", "Indore", "CBSC")
# obj.show_name()
# obj._show_school_address()

class XYZ(school):
    def __init__(self, name, address, board):
        super().__init__(name, address, board)

    def parent_method(self):
        self.show_name()
        self._show_school_address()
        self._school__show_board_name()


obj = XYZ("Shishukunj International", "Indore", "CBSC")
obj.parent_method()

