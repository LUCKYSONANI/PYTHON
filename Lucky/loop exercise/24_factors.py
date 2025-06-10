no=int(input("enter the value: "))
nof=0
sumf=0
for i in range(2,no):
    if(no%i==0):
         nof+=1
         print(i,f"is a factor of {no}")
         sumf=sumf+i
print(f"also 1 and {no} are factors of {no}")
print("the sum of factors is",sumf+no+2)
if(nof>=1):
    print(f"{no} is not a prime number")
else:
    print(f"{no} is a prime number")
    print(f"the number of factors are {nof}")

if(sumf+1==no):
    print(f"its a perfect number")
else:
    print(f"its not a perfect number")
    
         
        