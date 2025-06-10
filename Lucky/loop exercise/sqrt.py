val=int(input("enter the number:"))
for i in range(1,val):
    if(i*i>val):
        print('not possible')
        break
    if(i*i<val):
        print('not possible')
        break
    if(i*i==val):
        print("possible")
        break
    
        
        