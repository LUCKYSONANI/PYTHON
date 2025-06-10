i=1
val=0
cntn=0
cntp=0
sumo=0
sume=0
even=0
odd=0
for i in range(1,11):
    val=(int(input(f"enter the 10 digits to find which are odd , even , sum of odd/even , no. of odd/even{i} digit:")))
    if(val>0):
        cntp+=1
    elif(val<0):
        cntn+=1
    else:
        zero+=1
    if(val%2==0):   
        even+=1
        print(f"{val} is a even number")
        sumo=sumo+val
    
    elif(val%2!=0):
        odd+=1
        sume=sume+val
        print(f"{val} is a odd number")
    else:
        print("invalid input")
print(f"the sum of odd numbers is {sumo}""/n",f"the sum of even numbers is {sume}",f"the total number of even numbers is {even}",f"the total number of odd numbers is {odd}")
print(f"the positive numbers are{cntp}")
print(f"the negative numbers are{cntn}")


    
        