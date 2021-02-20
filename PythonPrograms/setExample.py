thisset={"maths", "physics", "chemistry"}
for s in thisset:
    print(s)

thisset.add("english")
print(thisset)
thisset.update(["hindi","tamil","sanskrit"])
print(thisset)

thisset.clear()
print(thisset)

del thisset

print(thisset)