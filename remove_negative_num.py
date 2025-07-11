num=[4,5,-3,6,7,-4,-9,5,-8]

filtered=[]

#Method 1
for n in num:
    if n>=0:
        filtered.append(n)

#Method 2
#filtered=list(filter(lambda n: n>=0, num))

#Method 3
#filtered=[item for item in num if item>=0]

print(filtered)