thisdict={
     "eid": "E001",
    "ename": "John",
    "edesignation": "CEO"
    }

print(thisdict)
print(thisdict["eid"]) #fetches the value
print(thisdict.get("eid")) #fetches the value

for x, y in thisdict.items():
  print(x, y)

for x in thisdict.keys():
  print(x)
  
for y in thisdict.values():
  print(y)

