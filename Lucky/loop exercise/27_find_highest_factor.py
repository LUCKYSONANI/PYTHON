no=int(input("enter the value: "))
nof=0
sumf=0
hf=0
for i in range(2,no):
    if(no%i==0):
         nof+=1
         print(i,f"is a factor of {no}")
         sumf=sumf+i
         hf=i
         print(i)
