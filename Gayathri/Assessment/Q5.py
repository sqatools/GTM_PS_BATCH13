"""Q5. Student Marks – Dictionary & Average
Write a Python program that:
•	Takes the name of a student and marks in 3 subjects as input.
•	Stores the data in a dictionary in the format:
{"name": <student_name>, "marks": [m1, m2, m3]}
•	Calculates the average marks of the student.
•	Prints the dictionary and the average.
"""

student_name = str(input("Enter Student name: "))
mark1 = int(input("Enter marks for English: "))
mark2 = int(input("Enter marks for Maths: "))
mark3 = int(input("Enter marks for Science: "))

#store above data as dictinoary
student= {
    "name": student_name,
     "marks": [mark1, mark2, mark3]
         }
#Average marks
sum_marks = sum(student["marks"])
no_subjects = len(student["marks"])
average = sum_marks / no_subjects

print("The student dictionary is: ",student)
print("The average marks of the student is:", round(average,2))

"""
output:
Enter Student name: gayathri
Enter marks for English: 92
Enter marks for Maths: 91
Enter marks for Science: 85
The student dictionary is:  {'name': 'gayathri', 'marks': [92, 91, 85]}
The average marks of the student is: 89.33

"""