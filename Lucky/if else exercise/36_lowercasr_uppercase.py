val1=input("enter an alphabet")
if(ord(val1)>=65 and ord(val1)<=90):
    print("its an upper case letter and its lower case form is",chr(ord(val1)+32))
elif(ord(val1)>=90 and ord(val1)<=122):
    print("its an lower case letter and its upper case form is",chr(ord(val1)-32))
else:
    print("imvalid input")

