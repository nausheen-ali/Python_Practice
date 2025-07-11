def delete_filelines(filename, line_num):
    with open(filename) as file:
        lines=file.readlines()

    if (line_num <= len(lines)):
        del lines[line_num - 1]
        with open(filename, "w") as file:
            for line in lines:
                file.write(line)
    else:
        print("Line", line_num, "not in file")
        print("File has", len(lines), "lines")

filename=input("Enter file:")
line_num=int(input("Enter line number:"))

delete_filelines(filename,line_num)