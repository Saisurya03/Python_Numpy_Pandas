a = (2,3,1,4,5)
print(a)
print(a[1])
b = list(a)
b[0] = 1
a = tuple(a)
a = tuple(b)
print(a)
for x in a:
	print(x)
print(len(a))
del a
a = (1,2,3)
b = (4,5,6)
c = a+b
print(c)
del a
a = (1)
print(a)
a = (1,)
a = (1,)*4
print(a)