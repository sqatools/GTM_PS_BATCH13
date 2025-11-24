"""
to achieve the data hiding, we have to define the variable and method name with single or double under score as prefix.
"""
class school:
    def __init__(self,name,location,type):
        self.school_name=name
        self._school_location=location
        self.__school_type=type
    def schoolname(self):
        print(self.school_name)
    def _schoolocation(self):
        print(self._school_location)
    def __schooltype(self):
        print(self.__school_type)
obj=school('Patapsco','Glenburg','Elementry')
obj.schoolname()
obj._schoolocation()
obj._school__schooltype()


