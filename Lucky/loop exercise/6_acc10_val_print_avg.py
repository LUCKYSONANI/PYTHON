i=1
val=0
avg=0
sum=0
for i in range(1,11):
    val=(int(input(f"enter the 10 digits to get their average,{i}:")))
    sum=sum+val
avg=sum/10
print(avg)