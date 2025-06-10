sum=0
for i in range(2,101):
    for j in range(2,i):
        if(j==2 and i%j==0):
            sum=2
        if(i%j!=0):
                sum+=i
print(sum)
            
            
            
            
            
            