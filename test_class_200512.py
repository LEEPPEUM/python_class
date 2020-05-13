class Athlete:
    def __init__(self, value='Jane'):
        self.thing = value;
    def getAthlete(self):
        return self.thing
a = Athlete()
print(a.getAthlete())
b = Athlete('Holy')
Athlete.__init__(a,'Holy')
print(b.getAthlete())


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    def innerPrint(self, infor):
        print(infor, self.x, self.y)

pt1 = Point()
print('Point01 Class', pt1.x, ',', pt1.y)
pt2 = Point(3,5)
print('Point02 Class', pt2.x, ',', pt2.y)
pt2.innerPrint('Point02 InnerPrint:')


class Employee:
    def __init__(self, name='null', salary=0):
        self.name = name 
        self.salary = salary
    def EmployeePrint(self, infor1, infor2):
        print(infor1, self.name, '/', infor2, self.salary)

emp1 = Employee()
print('Name: ', emp1.name, ',', 'Salary: ', emp1.salary)
emp2 = Employee("Zara", 2000)
print('Name: ', emp2.name, ',', 'Salary: ', emp2.salary)
emp3 = Employee("Manni", 5000)
print('Name: ', emp3.name, ',', 'Salary: ', emp3.salary)

emp2.EmployeePrint('Name ', 'Salary ')
emp3.EmployeePrint('Name ', 'Salary ')
