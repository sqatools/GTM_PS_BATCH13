
################# if- else condition #############
a=10
b=20
if a==b:
    print("both are same")
else:
    print("both are not same")

#################Program for finding Even and Odd number
num=20
if num%2==0:
    print("this is Even number:",num)
else:
    print("this is Odd number:",num)

################ if - elif --- else ###############(Nested if condition)
### Wrint program for interview process#########
round1="pass"
round2="fail"
round3="pass"
if round1=="pass":
    print("congrats 1st round is cleared")

    if round2=="pass":
        print("congrats 2nd round is cleared")

        if round3=="pass":
            print("congrats you are selected")
        else:
            print("failed in 3rd round")
    else:
        print("failed in 2nd time")

else:
    print("sorry you are not cleared the interview")

