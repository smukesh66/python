num1=int(input("Enter the number1 : "))
num2=int(input("Enter the number2: "))
sumDivisor = 0
ProductDivisor = 0
print("THE COMMON DIVISORS OF NUMBER ",num1," AND",num2," ARE -")
for i in range(1,min(num1,num2)+1):
    if num1%i== num2%i == 0:
      sumDivisor = sumDivisor + i  
ProductDivisor = ProductDivisor * i
if ("Product Divisor%sumDivisor==0"):
 print("YEAH")
else:
 print("NAH")
