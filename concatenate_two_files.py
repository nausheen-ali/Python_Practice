#Concatenate contents fo two file in a third file

def concatenate(filename1, filename2, new_filename):

    file1=open(filename1)
    file2=open(filename2)

    new_file=open(new_filename, "w")

    file1_contents=file1.read()
    file2_contents=file2.read()

    new_file.write(file1_contents)
    new_file.write(file2_contents)
    
    file1.close()
    file2.close()
    new_file.close()

filename1 = input("Enter file1:")
filename2 = input("Enter file2:")
newfile=input("Enter new file:")
concatenate(filename1, filename2, newfile)

#concatenate("f1.txt", "f2.txt", "f3.txt")