val2=float(input("enter the units"))
if(val2<50 or val2==50):
    print("the bill is",val2*0.5,"Rs")
elif(val2>50 and val2<151):
    print("the bill is",val2*0.75,"Rs")
elif(val2>150 and val2<251):
    print("the bill is",val2*1.2,"Rs")
elif(val2>250):
    val3=val2*1.5
    print("the bill is",val2*1.5,"surcharge=20%","total=",val3+val2*1.5*20/100)
    
    