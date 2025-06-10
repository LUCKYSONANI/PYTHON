val1=float(input("enter marks of maths"))
val2=float(input("enter marks physics"))
val3=float(input("enter marks of english"))
val4=float(input("enter marks of ip"))
val5=float(input("enter marks of chemistry"))
per=(val1+val2+val3+val4+val5)/5
if(per>90):
    print("A")
elif(per>80):
    print("B")
elif(per>70):
    print("C")
elif(per>60):
    print("D")
elif(per>50):
    print("E")  
elif(per>40):
    print("E")
elif(per<40):
    print("FAIL, better luck next time, practice required")
else:
    print("invalid input")      

