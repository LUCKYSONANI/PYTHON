i=1
sum=0
even=0
odd=0
sume=0
sumo=0
for i in range(1,21):
    if(i%2==0):
        sume=sume+i
        even+=1
    elif(i%2!=0):
        sumo=sumo+i
        odd+=1
    else:
        print("invalid INPUT")
print(f"the sum of odd numbers is:{sumo} , the sum of even numbers is:{sume}, the number of odd numbers are{odd}, the number of even numbers are {even}")
        

    
    