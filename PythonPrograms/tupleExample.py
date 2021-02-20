thistuple = ("apple", "banana", "cherry","banana") #allows duplicate values
print(thistuple)
print(thistuple[1])  #ordered
#thistuple[1] = "blackcurrant"  #unchangeable

for t in thistuple:
    print(t)
    
del thistuple
#print(thistuple)