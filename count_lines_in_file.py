def count_lines(filename):
    try:
        with open(filename) as file:
            lines=file.readlines()
            total_lines=len(lines)
            return total_lines
    except:
        print("File failed to open.")
        return None
    
filename=input("Enter file:")
l=count_lines(filename)

if l is not None:
    print("Total lines:",l)