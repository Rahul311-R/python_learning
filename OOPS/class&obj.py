class clg:

    def __init__(self):
        self.nodept = 8
        self.grade = 'A'

    def dept(self):
        self.nostud = 100
        self.nostaff = 15

    def out(self):
        print("values:",self.nodept,self.grade,self.nostaff)


s1 = clg()
s1.dept
s1.out()