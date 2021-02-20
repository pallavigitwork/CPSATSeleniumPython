
import xml.etree.ElementTree as ET

tree = ET.parse('sampledata.xml')
root = tree.getroot()
print(root.tag,root.attrib)

#traversing root - immediate child
for child in root:
    print(child.tag, child.attrib)
    
#accessing a specific node, as children are nested.
#example here we access all nodes of first country node
print("rank: ", root[0][0].text)
print("year: ", root[0][1].text)
print("gdpcc: ", root[0][2].text)

#to recurrsively iterate through all elements we use the following method
for neighbor in root.iter('neighbor'):
    print(neighbor.attrib)

 
#to access direct children of a node, we use findall method
for country in root.findall('country'):
    name = country.get('name') #fetch value of the value of the name attrib 
    rank = country.find('rank').text #fetch the data associated with the node rank.
    print(name, rank)
    
    
   

