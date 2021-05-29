s1 =  {65, 42, 78, 83, 23, 57, 29}
s2 = {67, 73, 43, 48, 83, 57, 29}

i = s1.intersection(s2)
for x in i:
    s1.remove(x)
    
print(s1)