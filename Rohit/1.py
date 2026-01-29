list =[1,20,8,6,19]

max_num = list[0]
for i in list:
 if i> max_num:
  max_num = i
print(max_num)
print(sorted(list))
   
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance   # private variable

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

acc = BankAccount(1000)
acc.deposit(500)
print(acc.get_balance())


s = "automation"
vowels = "aeiou"
count = 0

for ch in s:
    if ch in vowels:
        count += 1

print(count)



