# class_3

from class_3 import Class_3

c3 = Class_3()
c3.calculate()
print(c3.calculate())

import pickle

pickle.dump(c3, open("./c3.pkl", "wb"))
print('dump pickle')
c3_pkl = pickle.load(open("./c3.pkl", "rb"))
print('load pickle')
c3_pkl.calculate()
print(c3_pkl.calculate())
