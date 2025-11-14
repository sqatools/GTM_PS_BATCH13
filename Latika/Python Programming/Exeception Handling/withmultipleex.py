
def with_multiple_exception_handling(a,b,c,d):
    try:
        print("Addition is:",a+b)
        print("Division is:",a//c)
        assert c==d, "values are not equal"

    except AssertionError:
        print("Given inputs are not equal")
    except TypeError:
        print("All input no should be in nos.")
    except ZeroDivisionError:
        print("Can not dividable")
    except Exception as e:
        print("Exception message is",e)

with_multiple_exception_handling(10,20,30,50)