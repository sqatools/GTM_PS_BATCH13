class Teacher:
        def __init__(self,t_name,t_sub,t_phone_no):
            self.teacher_name=t_name
            self._teacher_subject=t_sub
            self.__teacher_phone_no=t_phone_no

        def show_teacher_name(self):
            print("Teacher name is :",self.teacher_name)

        def _show_teacher_subject(self):
            print("Teacher subject is :",self._teacher_subject)

        def __show_teacher_phone_no(self):
            print("Teacher phone no is :",self.__teacher_phone_no)
        """
        def show_phone_no(self):
            self.__show_teacher_phone_no()
        """


objteacher=Teacher("Rane","English",1234567890)
objteacher.show_teacher_name()
objteacher._show_teacher_subject()
#objteacher.show_teacher_phone_no()
objteacher._Teacher__show_teacher_phone_no()
