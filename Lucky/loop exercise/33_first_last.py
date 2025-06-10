v1=int(input("enter the number"))
ld=v1%10
while v1>0:
    fd=v1%10
    if(v1%10==1):
        fd=1
    v1=v1/10
    fd=1
print(fd+ld)
    
