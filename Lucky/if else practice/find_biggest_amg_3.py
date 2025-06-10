v1=int(input("enter the 1st no."))
v2=int(input("enter the 2nd no."))
v3=int(input("enter the 3rd no."))
if(v1>v2 and v1>v3):
    print(f"{v1} is greater than both {v2} and {v3} and biggest number is {v1}")
elif(v2>v1 and v2>v3):
    print(f"{v2} is greater than both {v1} and {v3} and biggest number is {v2}")
else:
    print(f"{v3} is greater")
    