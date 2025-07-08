num=int(input("Enter a number: "))
isPrime=True

if(num>1):
    for i in range(2,num):
        if(num%i)==0:
            isPrime=False
            break
    if isPrime:
        print(num, "is Prime number.")
    else:
        print(num, "is NOT Prime number.")

else:
    print("NUmber must be > 1")