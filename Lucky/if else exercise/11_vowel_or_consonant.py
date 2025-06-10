val1=input("enter an alphabet:")
if(65<(ord(val1))<90):
    print("its an upper case alphabet")
elif(97<ord(val1)<122):
    print("its an lower case alphabet")
else:
    print("invalid input, please enter an alphabet")
    