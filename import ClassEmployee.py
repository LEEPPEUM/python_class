
# from file_name(.py) import class_name
# 일반적으로 불러올 때, 반복적으로 많이 사용하는 경우

from ClassEmployee import Employee as emp

emp1 = emp("Zara", 2000)
emp2 = emp("Manni", 5000)

emp1.displayEmployee()
emp2.displayEmployee()




# import file_name(.py) as emp
# 파일 자체, 전체를 인스턴스화, 단순 한두번 사용 간단히 할때

import ClassEmployee as emp

emp1 = emp.Employee("Zara", 2000)

emp1.displayEmployee()




# from folder_name.file_name import class_name

from packages.ClassEmployee import Employee as emp

emp1 = emp("Zara", 2000)

emp1.displayEmployee()
