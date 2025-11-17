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
    col_area1 = None   # class variable

    def __init__(self, col_name, col_add, col_area):
        print("Welcome to the college")
        self.col_add1 = col_add
        self.col_name1 = col_name
        College.col_area1 = col_area   # store value in class variable

    def display_college_name(self):
        print("College Name:", self.col_name1)

    def display_college_add(self):
        print("College Address:", self.col_add1)

    @classmethod
    def display_college_area(cls):
        print("College Area:", cls.col_area1)

    @staticmethod
    def get_factorial(num):
        fact = 1
        for i in range(num, 0, -1):
            fact *= i
        return fact

colobj = College("Shivajirao Jondhale", "Dombivali East", "DSB Bank")
colobj.display_college_name()
colobj.display_college_add()
colobj.display_college_area()

output = colobj.get_factorial(5)
print("Factorial:", output)

