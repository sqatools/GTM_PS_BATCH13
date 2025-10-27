print("Write a program to count the occurrence of each character in a string")
print()

print("Using count()")

s="Hi Hello How are You"
count=s.count('H')
print(count)
#########################################################################
print()
print("Using Loop")
cnt=0
t='H'
for ch in s:
    if ch==t:
        cnt=cnt+1
print(cnt)

################################################################

