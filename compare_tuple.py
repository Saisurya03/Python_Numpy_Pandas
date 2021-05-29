A = (45, 45, 45, 45)
B = (10, 10, 45, 10)
x = []
f = 0
for i in range(len(A)):
    x.append(A[0])
x = tuple(x)

for i in range(len(A)):
    if x[i] != A[i]:
      f = 1
      
if f==1:
    print("Not Equal")
else:
    print("Equal")
    
x = []
for i in range(len(B)):
    x.append(B[0])
x = tuple(x)
f = 0
for i in range(len(B)):
    if x[i] != B[i]:
      f = 1
      
if f==1:
    print("Not Equal")
else:
    print("Equal")

