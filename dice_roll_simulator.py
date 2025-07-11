import random

dice = int(input("Enter no. of dice:"))

if (dice<=0):
    print("Must have atleast one dice.")
    quit()

roll=[]

for i in range (0,dice):
    face = random.randint(1,6)
    roll.append(face)

print(roll)