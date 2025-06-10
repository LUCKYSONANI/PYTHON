v1=int(input("enter the value"))
cnt=0
i=10
while i<=v1:
    if(v1/10>0):
        cnt+=1
    elif(v1/10==0):
        cnt=1
    elif(v1/10==1):
        cnt=2
    i-=1
    v1=v1/10
    
if(cnt>2):
    print(cnt)
else:
    print(cnt+1)
    
    


    
