import numpy as np

a = np.array([1,2,3,4,2,6,2,8,9])
b = np.where(a%2==0)
print(b)