val1=float(input("enter a number"))
val2=float(input("enter a number"))
if(val1==val2):
    print("same distance")
elif(val1>100):
    ax=val1-100
else:
    ax=100-val1
    if(val2>100):
        bx=val2-100
    else:
        bx=100-val2
if(ax>bx):
    print("b is near")
elif(bx>ax):
    print("a is near")  
else:
    print("same distance")
    print(0)      