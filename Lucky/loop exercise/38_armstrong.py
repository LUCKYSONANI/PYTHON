v1=int(input("enter the number"))
tmp=v1
sum=0
while v1!=0:
    dig=v1%10
    sum+=(dig*dig*dig)
    v1=v1//10
print(sum)
if(tmp==sum):
    print('armstrong')
else:
    print("not")
