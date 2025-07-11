def replace_line(filename, line_num, text):
    with open(filename) as file:
        lines=file.readlines()

    if (line_num <= len(lines)):
        lines[line_num-1] = text + "\n"

        with open(filename,"w") as file:
            for line in lines:
                file.write(line)

    else:
        print("Line", line_num, "not in file")
        print("File has", len(lines), "lines")


filename=input("Enter file:")
line_num=int(input("Enter line:"))
text=input("Enter text:")

replace_line(filename, line_num, text)