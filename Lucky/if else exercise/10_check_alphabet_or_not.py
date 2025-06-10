val1=input("enter a digit or alphabet or special character:")
if(90>ord(val1)>65 or 122>ord(val1)>97):
    print("alphabet")
elif(47>ord(val1)>32 or 100>ord(val1)>58 or 96>ord(val1)>91 or 127>ord(val1)>123):
    print("special character")
else:
    print("digit")