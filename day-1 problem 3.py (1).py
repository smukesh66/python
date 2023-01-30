def happynumber(num):
   sum=0
   rem=0
   while(num>0):
       rem=num%10;
       sum=sum+(rem*rem);
       num=num//10;
   return sum
num=int(input("Enter a number : "))
result=num
while(result!=1 and result!=4):
    result=happynumber(result);
if(result==1):
    print(str(num)+" is a happy number.")
elif(result==4):
    print(str(num)+" is not a happy number.")
