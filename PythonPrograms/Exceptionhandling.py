try:
    fo = open("d:\\write1.txt", "r")
    for line in fo:
        print(line)
    fo.close()
    #fh.readline("This is my test file for exception handling!!")
except Exception:
    print("Error: can\'t find file or read data")
else:
    print("Written content in the file successfully")
    fo.close()
finally:
    print("always execute")

print("outside code")