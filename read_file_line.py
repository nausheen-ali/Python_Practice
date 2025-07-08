filename=input("Enter file name: ") #file.txt
line_num=int(input("Enter line number: "))

file=open(filename, "r")
lines = file.readlines()
file.close()

total_lines=len(lines)
if(line_num > total_lines):
    print(total_lines, "lines in file")
    print("Can't read line", line_num, "!")
else:
    line=lines[line_num-1].rstrip('\n')
    print(line)