import random 
def flip_coin():
    return random.choice(["Heads", "Tails"])
print(flip_coin(), "\n")


heads=0
tails=0

for i in range(10):
    result=flip_coin()
    print("Flip " + str(i+1)+ ": " + result)

    if result=="Heads":
        heads+=1
    else:
        tails+=1

print("\nTotal heads:", heads)
print("Total Tails:", tails)
