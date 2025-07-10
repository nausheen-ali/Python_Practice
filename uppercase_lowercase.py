#count number of uppercase and lowercase characters in a string

def count_lower(text):
    count=0
    for char in text:
        if(char.islower()):
            count+=1
    return count

def count_upper(text):
    count=0
    for char in text:
        if(char.isupper()):
            count+=1
    return count

text=input("Enter text:")

upcount=count_upper(text)
lowcount=count_lower(text)

print("Total number of uppercase characters:", upcount)
print("Total number of lowercase characters:", lowcount)