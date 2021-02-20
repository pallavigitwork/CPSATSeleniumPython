
list1 = ['physics', 'chemistry', 1997, 2000]
list2 = [1, 2, 3, 4, 5, "apple", 7 ]

print("list1[0]: ", list1[0])
print("list2[1:5]: ", list2[1:5])

#update item in the list.
list1[3]=100
print(list1)

#Delete item from list
del list2[3] #element at the index
print(list2)

list2.remove("apple") #actual element
print(list2)

#Iterate through List
for i in list2:
    print(i)
    
#List Functions
print("Length of list2:" ,len(list2))
print("max element of list2:" ,max(list2))
print("min element of list2:" ,min(list2))
print("position of element in list", list1.index(1997))
list2.reverse()
print("reverse of list2", list2)





