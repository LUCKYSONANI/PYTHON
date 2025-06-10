# def num(a):
#     a=int(input("enter the number to be checked(odd or even):"))
#     if(a%2==0):
#         print(num(a),'is even')
#     else:
#         print(num(a),'is odd')
# num(0)    
def num(a):
    if a % 2 == 0:
        print(a, 'is even')
    else:
        print(a, 'is odd')

a = int(input("Enter the number to be checked (odd or even): "))
num(a)