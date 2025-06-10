val=int(input("enter the value"))
fact=1
sum=0
tmp=val
dig=0
while val>0:
    dig=val%10
    fact=1
    while dig>0:
        fact=fact*dig
        dig-=1
    val=val//10
    sum=sum+fact
if(sum==tmp):
    print("strong number",tmp)
else:
    print("not strong")
    
    
        