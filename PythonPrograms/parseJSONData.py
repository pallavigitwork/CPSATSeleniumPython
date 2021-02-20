import json

#READ from file
with open("sampledata.json", "r") as read_file:
    data = json.load(read_file) # a list of dict vals
   # print(data)
    #print(data["children"][0])
    child=data["children"][1]
    print(child)
    print(child["firstName"])
    print(child["age"])
    

#accessing an array in json
print(data["hobbies"])
for hob in data["hobbies"]:
    print(hob)
    
    