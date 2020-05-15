# class Class_3:
#     def __init__(self, x=0):
#         self.x = x
#     def calculate(self):
#         return self.x+(self.x+2)


class Class_3:
    def __init__(self, x1=0, x2=2):
        self.x1 = x1
        self.x2 = x2
    def calculate(self):
        self.x2 = self.x1 + 2
        return self.x1 + self.x2

