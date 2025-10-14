round1= "pass"
round2 = "pass"
round3 = "pass"

if round1 == "pass":
    print("round 1 is cleared")
    if round2 == "pass":
        print("round 2 is cleared")
        if round3 == "pass":
            print("round 3 is cleared")
        else:
            print("round 3 not cleared")
    else:
     print("round 2 not cleared")
else:
    print("round 3 not cleared")


