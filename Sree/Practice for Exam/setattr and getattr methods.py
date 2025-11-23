class student:               ## setattr() & getattr()
    def __init__(self):
        pass              #  # No predefined instance variables
obj=student

setattr(obj,'name','Ram')
setattr(obj,'age',20)
setattr(obj,'school','Elementry')

print('Student Name',getattr(obj,'name'))
print('Age',getattr(obj,'age'))
print('School:',getattr(obj,'school'))