import matplotlib.pyplot as mp
values = [0,5,8,9,2,0,3,10,4,7]
ax = mp.axes()
ax.set_xlim([0,11])
ax.set_ylim([1,11])
ax.set_xticks([1,2,3,4,5,6,7,8,9,10])
ax.set_yticks([0,1,2,3,4,5,6,7,8,9,10])
ax.grid()
mp.plot(range(1,11),values)
mp.show()
