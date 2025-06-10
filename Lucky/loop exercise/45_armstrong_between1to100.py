suma=0
for v in range(1,1001):
    tmp=v
    sum=0
    while v!=0:
        dig=v%10
        sum+=dig*dig*dig
        v=v//10
    if(tmp==sum):
        print('armstrong',tmp)
        suma+=tmp
print("sum of armstrong no. are:",suma)
