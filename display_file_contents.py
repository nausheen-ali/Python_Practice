filename=input("Enter file:")
try:
    file=open(filename, "r")
    contents=file.read()
    print(contents)
    file.close()
except:
    print("Error reading file.")