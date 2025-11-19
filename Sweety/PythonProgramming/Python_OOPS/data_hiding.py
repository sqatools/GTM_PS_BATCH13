"""
to achieve the data hiding, we have to define the variable and method name with single or double under score as prefix.
"""
class School:
    def __init__(self, s_name, s_address, s_board, s_subcount, s_studentcount):
        self.school_name = s_name
        self.school_address = s_address
        self.school_board = s_board
        self._subcount = s_subcount
        self.__studentcount = s_studentcount

    def show_school_name(self):
        print("School Name: ", self.school_name)

    def _show_school_address(self):
        print("School Address: ", self.school_address)

    def __show_school_board(self):
        print("School Board: ", self.school_board)

    def show_sub_count(self):
        print("Subject Count: ", self._subcount)

    def show_student_count(self):
        print("Student Count: ", self.__studentcount)

obj = School("MG Convent", "Andheri", "CBSC",'9', '2000')

# when we define any variable/method with single/double underscore as prefix, then
# those variable/method will not show in suggest list.

obj.show_school_name()

# access variable/method with single underscore as prefix: user can access directly.
obj._show_school_address()

# access variable/method with double underscore as prefix: user has to follow a pattern to access method or variable
# obj._class__variable/method
obj._School__show_school_board()

obj.show_sub_count()
obj.show_student_count()
