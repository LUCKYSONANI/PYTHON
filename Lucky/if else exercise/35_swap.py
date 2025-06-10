val1=float(input("enter first number"))
val2=float(input("enter second number"))
tmp=val2
if(val1==val2):
    print("same variable")
elif(val1!=val2):
    val2=val1
    val1=tmp
    print("the variables are:",val1,val2)

    
    