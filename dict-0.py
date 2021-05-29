a = {'name':'ABC', 'age':12,'email':'a@a.com'}
print(a)
for i in a:
	print(i)
for i in a:
	print(a[i])
for i,j in a.items():
	print(i,j)
for i in a.values():
	print(i)
len(a)
a['name'] = 'PQR'
print(a)
a.pop('name')
print(a)
print(a.get('age'))
del a
print(a.get('age'))	

