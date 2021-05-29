list1 = ["Hello ", "Hi "]
list2 = ["Dear", "Sir"]
output = []
x = 0

for i in list1:
  for j in list2:
    output.append(i + " " + j)
  x = x+1
  
print(output)