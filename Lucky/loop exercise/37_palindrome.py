v1=int(input("enter the number"))
rev=0
tmp=v1
while v1>0:
    dig=v1%10
    rev=rev*10+dig
    v1=v1//10
if(rev==tmp):
    print("palindrome")
else:
    print("not a plaindrome")