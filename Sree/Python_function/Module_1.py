Var_x=500
def add(x,y):
    a=x+y
    print(Var_x + a)
def Mul(x,y):
  b=x*y
  print("mulval:",b)

def Mul(*args):
    result=1
    for i in args:
        result *=i
        print('Mul_val:',result)
    print('Mul_val_sum:', result)
def Ave(*args):
    print("Aveval:",sum(args)//len(args))








