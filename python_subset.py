a = {27, 43, 34}
b = {34, 93, 22, 27, 43, 53, 48}
x = list(b)
if a.issubset(b):
	for i in a:
		x.remove(i)
		
b = set(x)
print(b)