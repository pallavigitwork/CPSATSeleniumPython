#write a File
fw=open("d:\\write.txt", "w")
fw.write("Dear God, Please ensure that\n")
fw.write("Peace be upon us, prospertiy be upon us\n")
fw.write("and u be happy up there!\n")
fw.close()
fw=open("C:\Users\lakshmi_doddapaneni\Desktop\write.txt","w")

#read file
fo = open("d:\\write.txt", "r")
for line in fo:
    print(line)
fo.close()

#append a File
fw=open("d:\\write.txt", "a")
fw.write("and let us stay happy down here!!")
fw.close()

#read again
print("\nAfter Append")
fo = open("d:\\write.txt", "r")
for line in fo:
    print(line)
fo.close()


