def num(a,b):
    a=(int(input("enter the number")))
    b=(int(input("enter the number")))
    operator=input("enter the operator:(+ or - or / or *)")
    if(operator=='+'):
        return a+b
    elif(operator=='-'):
        return a-b
    elif(operator=='/'):
        return a/b
    elif(operator=='*'):
        return a*b
num()