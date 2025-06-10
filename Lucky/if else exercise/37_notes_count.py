val1=float(input("enter the currency (10rs note,50rs note,100rs note,500rs note)"))
val2=int(input("enter the quantity of notes"))
if(val1==10):
    print("total amount is",val2*10,"the amount is in 10rs notes")
elif(val1==50):
    print("total amount is",val2*50,"the amount is in 50rs notes")
elif(val1==100):
    print("total amount is",val2*100,"the amount is in 100rs notes")
elif(val1==500):
    print("total amount is",val2*500,"the amount is in 500rs notes")
else:
    print("invalid input")
    