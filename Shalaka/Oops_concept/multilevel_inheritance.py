class father:
    def __init__(self, f_name, f_business):
        self.father_name = f_name
        self.father_business = f_business

    def father_details(self):
        print(self.father_name)
        print(self.father_business)


class mother:
    def __init__(self, m_name, m_business):
        self.mother_name = m_name
        self.mother_business = m_business

    def mother_details(self):
        print(self.mother_name)
        print(self.mother_business)


class son(father, mother):

    def __init__(self, s_name, s_job, f_name, f_business, m_name, m_business):
        super().__init__(f_name, f_business)
        self.mother_name = m_name
        self.mother_business = m_business
        self.son_name = s_name
        self.son_job = s_job

    def son_details(self):
        print(self.son_name)
        print(self.son_job)

    def family_details(self):
        self.son_details()
        self.father_details()
        self.mother_details()


obj = son("Rahul", "QA", "Ram", "Tiles", "Suman", "Fashion")
obj.family_details()
