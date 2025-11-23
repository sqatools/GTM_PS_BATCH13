"""
when one operator perform multiple task, then it is called operator overloading
                        e.g. plus(+) operator can add 2 int, it can add 2 string, it can add 2 list as well
                        integer is a "class" add method .add, .sub ....
                        # operator overloading : when we call any operator, then python has some magic the called behind the seen to perform this operation
# with different operator and data types.

"""
n1=10
n2=20
print(n1.__add__(n2))
print(n1.__sub__(n2))
print(n1.__mul__(n2))
print(n1.__divmod__(n2))


str1='Hello'
str2= 'Ram'
print(str1.__add__(str2))
