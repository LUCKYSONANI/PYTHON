i=1
val=0
cntn=0
cntp=0
for i in range(1,11):
    val=(int(input(f"enter the 10 digits to find which are positives,{i} digit:")))
    if(val>0):
        cntp+=1
        print(f"{i} is positive")
    elif(val<0):
        cntn+=1
        print(f"{i} is negative")
    else:
        print("zero or invalid input")
print(f"the number of negative numbers are {cntn} and the positive numbers are {cntp}")