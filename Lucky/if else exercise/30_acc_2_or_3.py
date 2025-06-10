val1=input("enter the number 2 or 3    :")
if(val1=='2'):
    val2=float(input("enter the number"))
    val3=float(input("enter the number"))
    print("sum is",val2+val3)
elif(val1=='3'):
    val2=float(input("enter the number"))
    val3=float(input("enter the number"))
    val4=float(input("enter the number"))
    print("the sum is",val2+val3+val4)
else:
    print("invalid input")
    