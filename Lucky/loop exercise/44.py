no=int(input("enter the value: "))
nof=0
sumf=0
for i in range(2,no):
    if(no%i==0):
        g=i
        nof+=1
        sumf=sumf+i
        for g in range(2,101):
            for j in range(2,g):
                if(g%j!=0):
                    print(f"{g} is a prime factor of{no}")
if(nof>=1):
    print(f"{no} is not a prime number")
else:
    print(f"{no} is a prime number")
