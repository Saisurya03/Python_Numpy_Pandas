import matplotlib.pyplot as mp

values = [1,5,8,9,2,0,3,10,4,7]
values2 = [3,8,9,2,1,2,4,7,6,6]
mp.plot(range(1,11),values,"--")
mp.plot(range(1,11),values2,":")
mp.show()