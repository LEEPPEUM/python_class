from packages.ClassEmployee import Employee as emp

emp1 = emp("Zara", 2000)
emp1.displayEmployee()

import pickle

pickle.dump(emp1, open("./emp1.pkl", "wb"))     # ? 지금 바로 .pkl 파일명이랑 권한을 만들어주고 있는건가 ?
# 인스턴스화 된 emp1을 그대로 영구적 저장.
print('dump pickle')

emp1_pkl = pickle.load(open("./emp1.pkl", "rb"))
print('load pickle')

emp1_pkl.displayEmployee()