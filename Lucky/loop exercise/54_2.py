# i=1
# while i<=5:
#     j=i
#     while j<=5:
#         print('*')
#         j+=1
#     i+=1

# for i in range(1,6):
#     j=i
#     while j<=5:
#         print(j*'*')
#         j+=1

for i in range(1,6,1):
    print('1'*5)
#or
for i in range(5,0,-1):
    print('1'*5)
    

for i in range(1,6,1):
    print('1'*i)
    

for i in range(5,0,-1):
    print('1'*i)


for i in range(5,0,-1):
    for j in range(i+1,6):
        print(j,end='')
    print
    
