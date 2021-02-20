#list
#ordered, indexed, changeable, duplicate. 
demoList = ["apple", "banana", "cherry", "banana"]
print(demoList) #ordered
print(demoList[2]) #indexed
demoList.insert(3,"yellow")#changeable
print(demoList)
demoList.insert(2,"yellow")#duplicate
print(demoList)

#tuple
#ordered, indexed, duplicate, doesn't allow change
demoTuple = ("apple", "banana", "cherry","cherry")
print(demoTuple)
print(demoTuple[1])

#a tuple is a list which doesn't allow change.


#set
#unordered. unindexed. no duplicate,changeable.
demoSet = {"apple", "banana", "cherry", "orange", "grapes"}
print(demoSet) #unordered
#print(demoSet[2]) #throwserror
demoSet.add("pineapple")
print(demoSet)#change
demoSet.add("pineapple")#doesn't add. 
print(demoSet)#change

#unordered, indexed, changeable, no duplicates
demoDict =    {
  "1": "Somya",
  "2": "Fiona",
  "3": "Diana",
  "4": "Pont",
  "5": "freida"
}
print(demoDict.get("2")) #returns the value associated with the key
demoDict["6"]="Samar"  #adding information
print(demoDict) 
demoDict["6"]="Samar"  #didnot change
print(demoDict)