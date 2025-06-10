val=int(input("enter the value"))
multi=1
binary=0
rem=0
while val>0:
    rem=val%2
    binary=binary+(rem*multi)
    val=val//2
    multi=multi*10
print(binary)