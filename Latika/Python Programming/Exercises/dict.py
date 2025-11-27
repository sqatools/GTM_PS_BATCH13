
student_name=input("Enter the student name :")
m1 = int(input("Enter the marks for subj 1 :"))
m2 = int(input("Enter the marks for subj 2 :"))
m3 = int(input("Enter the marks for subj 3 :"))

student = {
    "name":"student_name",
    "marks":[m1,m2,m3]
}

sum_marks = m1+m2+m3
avg_marks = sum_marks/3

print(student_name,":","Average of marks :",avg_marks)


