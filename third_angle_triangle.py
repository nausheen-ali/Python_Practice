angle1=int(input("Enter first angle:"))
angle2=int(input("Enter second angle:"))

if ((angle1>0 and angle1<180) and (angle2>0 and angle2<180) and (angle1+angle2)<180):
    angle3=180-angle1-angle2
    print("Third angle:", angle3)
else:
    print("Angle 1 or/and Angle 2 are invalid.")