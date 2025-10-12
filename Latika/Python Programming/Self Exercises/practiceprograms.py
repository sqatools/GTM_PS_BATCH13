##############################Self Practices########################

print("Program to get the median of given numbers.")

values=[10,20,30,40,50]
values.sort()
n=len(values)
if n%2==1:
    median_value=values[n//2]
else:
    median_value=(values[n//2-1]+values[n//2])/2
print("The Median Value is :",{median_value})

######################################################################

rows = 5  # Number of rows

for i in range(1, rows + 1):  # Loop for rows
    for j in range(i):  # Loop for columns (stars)
        print("*", end=" ")  # Print star
    print()  # Move to the next line


##################################################################


number=5
for i in range(number,0, - 1):
    for j in range(i):
        print("*",end=" ")
    print()
