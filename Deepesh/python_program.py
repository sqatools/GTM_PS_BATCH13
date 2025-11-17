# Take marks through the user
marks = int(input("Enter marks: "))
# Assign grades based on marks
if marks<40:
    # marks is less than 40 then print Fail
    print("Fail")
elif marks>=40 and marks>=50:
    # marks is greater than 40 and less than 50 then got C grade.
    print("Grade C")
elif marks>50 and marks<=60:
    #  marks is greater than 50 and less than 60 then got B grade.
    print("Grade B")
elif marks>60 and marks<=70:
    #  marks is greater than 60 and less than 70 then got A grade.
    print("Grade A")
elif marks>70 and marks<=80:
    #  marks is greater than 70 and less than 80 then got A+ grade.
    print("Grade A+")
elif marks>80 and marks<=90:
    #  marks is greater than 80 and less than 90 then got A++ grade.
    print("Grade A++")
elif marks>90 and marks<=100:
    #  marks is greater than 90 and less than 100 then got Excellent grade.
    print("Excellent")
else:
    # marks is greater than 100 than consider as invalid number..
    print("Invalid marks")
    
# Define a list
my_list = ['apple', 'banana', 'cherry']

# Use enumerate to get index and element
for index, element in enumerate(my_list):
    print(f"Index: {index}, Element: {element}")