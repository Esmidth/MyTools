__author__ = 'Esmidth'

import pickle

with open('mydata.pickle', 'wb') as mysavedata:
    pickle.dump([1, 2, 'three'], mysavedata)

with open('mydata.pickle', 'rb') as myrestoredata:
    a_list = pickle.load(mysavedata)

print(a_list)