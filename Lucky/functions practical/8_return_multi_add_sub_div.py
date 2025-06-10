# def num():
#     a=(int(input("enter the number")))
#     b=(int(input("enter the number")))
#     operator=input("enter the operator:(+ or - or / or *)")
#     if(operator=='+'):
#         print(a+b)
#     elif(operator=='-'):
#         print(a-b)
#     elif(operator=='/'):
#         print(a/b)
#     elif(operator=='*'):
#         print(a*b)
#     else:
#         print("invalid operator")
# num()
def num(a,b):
    a=(int(input("enter the number")))
    b=(int(input("enter the number")))
    add=a+b
    sub=a-b
    div=a/b
    mul=a*b
    return add,sub,div,mul
    # operator=input("enter the operator:(+ or - or / or *)")
    # if(operator=='+'):
    #     return a+b
    # elif(operator=='-'):
    #     return a-b
    # elif(operator=='/'):
    #     return a/b2
    # elif(operator=='*'):
    #     return a*b
result=num(10,2)
add,mul,div,sub = result
print(add,sub,mul,div)
# print(num(0,0))
