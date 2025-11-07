class summa:
    def line1(self):
        print("This is line one")
class summa2(summa):
    def line2(self):
        print("This is line two")

a = summa2()
a.line1()
a.line2()