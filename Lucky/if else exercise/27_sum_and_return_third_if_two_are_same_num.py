val1=float(input("enter a number"))
val2=float(input("enter a number"))
val3=float(input("enter a number"))
sum=val1+val2+val3
if(val1==val2):
    print(val3)
elif(val2==val3):
    print(val1)
elif(val1==val3):
    print(val2)
else:
    print(sum)
