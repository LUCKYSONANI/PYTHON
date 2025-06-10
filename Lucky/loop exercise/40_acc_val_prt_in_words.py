val=int(input("enter the value"))
rev=0
dig=0
while(val>0):
    rev=(rev*10)+val%10
    val=val//10
while(rev>0):
    dig=rev%10
    if(dig==0):
        print('zero')
    elif(dig==1):
        print('one')
    elif(dig==2):
        print('two')
    elif(dig==3):
        print('three')
    elif(dig==4):
        print('four')
    elif(dig==5):
        print('five')
    elif(dig==6):
        print('six')
    elif(dig==7):
        print('seven')
    elif(dig==8):
        print('eight')
    elif(dig==9):
        print('nine')
    rev=rev//10
        
        
    