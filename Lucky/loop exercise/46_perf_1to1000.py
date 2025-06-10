for no in range(1,1001):
    nof=0
    sumf=0
    sump=0
    for i in range(2,no):
        if(no%i==0):
            sumf=sumf+i
    if(sumf+1==no):
        print(f"its a perfect number{no}")
        sump+=sumf+1
        print("the sum of perfect numbers is;",sump)
    else:
        print(f"its not a perfect number")