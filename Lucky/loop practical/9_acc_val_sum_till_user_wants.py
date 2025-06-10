ans='y'
val=0
sum=0
while(ans=='y' or ans=='Y'):
    val=int(input("enter a value:"))
    sum=sum+val
    ans=input("do you want to add more?(y/n):")
    print(f"sum is {sum}")
    