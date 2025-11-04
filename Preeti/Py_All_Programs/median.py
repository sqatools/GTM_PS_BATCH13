'''Python program to get the median of given numbers.
Note: all the numbers should be arranged in ascending order
Formula : (n+1)/2
n = Number of values
Input : [45, 60, 61, 66, 70, 77, 80]
Output:  66
'''
#input=[45,60,61,66,70,77,80]
input.sort()
n=len(input)
print(input[n//2])





