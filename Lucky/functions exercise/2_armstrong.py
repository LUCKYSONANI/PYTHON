# def val():
#     tmp=v1
#     sum=0
#     while v1!=0:
#         dig=v1%10
#         sum+=(dig*dig*dig)
#         v1=v1//10
#     print(sum)
#     if(tmp==sum):
#         print('armstrong')
#     else:
#         print("not")
# v1=int(input("enter the number to be checked(armstrong or not):"))
# val()
#     tmp = v1
#     sum = 0
#     while v1 != 0:
#         dig = v1 % 10
#         sum += (dig * dig * dig)
#         v1 = v1 // 10
#     print(sum)
#     if tmp == sum:
#         print('armstrong')
#     else:
#         print("not")
# v1 = int(input("enter the number to be checked(armstrong or not):"))
# val(v1)
def val(v1):
    tmp = v1
    sum = 0
    while v1 != 0:
        dig = v1 % 10
        sum += (dig * dig * dig)
        v1 = v1 // 10
    print(sum)
    if tmp == sum:
        print('armstrong')
    else:
        print("not")
v1 = int(input("enter the number to be checked(armstrong or not):"))
val(v1)