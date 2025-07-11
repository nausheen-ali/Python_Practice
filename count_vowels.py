text=input("Enter text:")

count=0

for char in text:
    if (char in 'aeiouAEIOU'):
        count+=1

print("Total vowels:", count)