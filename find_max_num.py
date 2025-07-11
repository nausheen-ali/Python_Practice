#Finding maximum number in a list without using max function

list = [3,6,4,9,1]
max=list[0]
for n in list:
    if n>max:
        max=n
    
print("Max:", max)