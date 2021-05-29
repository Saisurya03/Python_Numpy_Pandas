l = [1,2,3,4,5,6,7]
print("Input list: {}".format(l))
x = 0
for i in l:
    i = i ** 2
    l[ x ] = i 
    x = x + 1
print("Output list: {}".format(l))