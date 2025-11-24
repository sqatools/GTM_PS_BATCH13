"""
 Create a Python class called Person with attributes name and age?.
"""
class person:
    def __init__(self,name,age):
        self.personname=name
        self.personage=age
    def display_details(self):
        print('person_name',self.personname)
        print('person_age',self.personage)

print('-'*44)
"""
 Create a Python class called Student that inherits from the Person class.
Add attributes student_id and grades. Include a method to print the student’s name, age, and student ID.
"""
class student(person):
    def __init__(self, student_id, grade, name, age):
        super().__init__(name, age)
        self.student_id=student_id
        self.grade=grade
    def studentid_grade(self):
        print("student_id:",self.student_id)
        print('grade:',self.grade)
    def studentdetails(self):
        self.display_details()
        self.studentid_grade()


obj=student(29034,'5th','Shreya',25,)
obj.studentdetails()
print('_'*44)
"""
Create a Python class called Cat that inherits from the Animal class.
Add attributes breed and weight. Include a method to print the cat’s name, color, breed, and weight.
"""
class Animal:
    def __init__(self,name,color):
        self.name=name
        self.color=color
    def show_details(self):
        print('Name',self.name)
        print('color:',self.color)
class cat(Animal):
    def __init__(self, name, color,breed,weight):
        super().__init__(name, color)
        self.breed=breed
        self.weight=weight
    def show_detail(self):
        super().show_details()   ##self.show_details
        print('Breed:',self.breed)
        print('weight:',self.weight)

obj=cat('Jimmy','Greyishwhite','breed','30 pounds')
obj.show_detail()

print('-'*44)
"""
classcalled BankAccount_attributes=account_number&balance.Include methods to deposit and withdraw money from the account.
"""
class BankAccount:
    def __init__(self,account_no,Balance):
        self.accountnumber=account_no
        self.balance=Balance
    def show_account(self):
        print("account_no:",self.accountnumber)
        print("Balance:",self.balance)

    def deposit(self,amount):
        self.balance +=amount
        print('deposited amount:',amount,'new balance',self.balance)
    def withdrawl(self,amount):
        self.balance -=amount
        print("withdrawamount:",amount,'new balance:',self.balance)

obj=BankAccount(8976543211,500000)
obj.show_account()
obj.deposit(1000)
obj.withdrawl(500)
print('-'*44)
"""
shopping cart-add item, remove item
"""
class shoppingcart:
    def __init__(self):
        self.items=[]
        self.total_cost=0
    def add_item(self,item,cost):
        self.items.append(item)
        self.total_cost +=cost
    def remove_item(self,item,cost):
        self.items.remove(item)
        self.total_cost -=cost
    def calculate_total_cost(self):
        return self.total_cost
cart=shoppingcart()
cart.add_item('kids pant',10)
cart.add_item('kids shirt',8)
cart.add_item('women shirt',20)
cart.add_item('women jocket',50)
cart.add_item('bedding set',80)
cart.remove_item('women shirt',20)
cart.remove_item('kids shirt',8)
totalcost=cart.calculate_total_cost()
print("Items in cart:", cart.items)
print("Total Cost:", totalcost)




