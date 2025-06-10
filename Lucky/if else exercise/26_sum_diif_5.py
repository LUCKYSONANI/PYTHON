val1=float(input("enter a number"))
val2=float(input("enter a number"))
if(val1==5):
    print(f"{val1} is first digit and it is five")
elif(val2==5):
    print(f"{val2} is second digit and it is five")
elif(val1+val2==5):
    print("sum is 5")
elif(val1-val2==5 or val2-val1==5):
    print("difference is 5")
else:
    print("invalid")
    