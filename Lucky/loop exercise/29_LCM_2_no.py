v1=int(input("enter the value"))
v2=int(input("enter the value"))
i=2
while( v1>=i and v2>=i):
    if(v1%i==0 and v2%i==0):
        hcf=i
        break
    i+=1
print(hcf)