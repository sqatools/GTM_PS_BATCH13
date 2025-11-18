try:
  a =20
  b="hi"
print("addition:",a+b)

except Exception as e:
print(e)
print
########## try except-else #############
def handle_nested_exception(a,b,c):
    try:
        print("addition:",a+b)
        try:
            div=b//c
            print("division:",div)
        except Exception as e2:
            print(e2)
            print("division with zero not allowed")
    except Exception as e1:
        print(e1)




