"""
There are two types of constructors.
1. Default constructor
    def __init__(self)
    pass
2. Parameterized constructor
    def __init__(param1,param2)
    pass

"""
class College:
    def __init__(self,col_name,col_add):
        print("Welcome to the college")
        self.col_add1=col_add
        self.col_name1=col_name
    def display_college_name(self):
        print("College Name",self.col_name1)

    def display_college_add(self):
        print("College Add",self.col_add1)

colobj=College('Shivajirao Jondhale','Dombivali east')
colobj.display_college_name()
colobj.display_college_add()

