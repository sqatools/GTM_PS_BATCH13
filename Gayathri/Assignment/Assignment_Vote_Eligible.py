#write a python program to check if a person is eligible for vote or not
person_age = -1
if person_age > 0 and person_age < 18:
    print("person is not authorized to vote, age is :",person_age)
elif person_age >  18 or person_age == 18 :
    print("person is authorized to vote, voting age is :",person_age)
else:
    print("Enter a valid age")