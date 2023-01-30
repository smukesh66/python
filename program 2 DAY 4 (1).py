t=int(input("enter total users="))
if(t==0):
    print("invalid input")
    t=t=int(input("enter total user="))
elif(t<0):
    print("invalid input")
    t=t=int(input("enter total users="))
s=int(input("enter saff users="))
n=(s//3)
if(t<s):
    print("invalid input")
elif(t==s):
    print("student user are=",t-(s-n))
else:
    print("student users are=",t-s-n)
