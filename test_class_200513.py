
class Employee:
    empCount = 0
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1
        # Employee.empCount = empCount + 1 을 간소화 시킨 것.
    def displayCount(self):
        print("Total Employee ",Employee.empCount)
    def displayEmployee(self):
        print("Name : ", self.name, ", Salary: ", self.salary)


# 이것은 변수에 데이터(값)를 집어 넣는 과정.
emp1 = Employee("Zara", 2000);
emp2 = Employee("Manni", 5000)

# 이것은 emp1이라는 ("Zara", 2000) 데이터를 가진 변수에다가 
# class인 Employee를 실행시키는데 
# class가 가진 3개의 function 중에서 displayEmployee를 선택한 것.
emp1.displayEmployee();
emp2.displayEmployee()

# empCount는 function 외부에 초기값 변수를 선언해준 건데
# 데이터의 레코드의 수에 따라 class, function이 돌아가니까
# run이 몇 번 돌아갔는지, 데이터 레코드의 수를 셀 수 있다.
print("Total Employee ", Employee.empCount)
