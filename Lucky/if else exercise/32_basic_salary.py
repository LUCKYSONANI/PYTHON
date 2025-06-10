val1=float(input("enter the basic salary"))
if(val1<10000 or val1==10000):
    print("HRA= 20% , DA=80%")
elif(val1<20000 or val1==20000):
    print("HRA=25% , DA=90%")
elif(val1>20000):
    print("HRA=30% , DA=95%")
else:
    print("invalid input")
    