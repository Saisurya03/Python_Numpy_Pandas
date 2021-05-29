dictionary1 = {
  "name": "abc",
  "age":25,
  "salary": 15000,
  "city": "Rajkot"
  
}
dictionary = dictionary1.copy()
for x,y in dictionary1.items():
    if x == "name":
        print(dictionary.pop(x))
    elif x == "salary":
        print(dictionary.pop(x))
        
dictionary1 = dictionary		
print(dictionary1)