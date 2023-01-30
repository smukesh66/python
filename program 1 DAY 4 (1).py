n=int(input("enter a number: "))
for i in range(1,n+1):
    if i%3==0 and 1%5==0:
        print("FizzBuzz")
    elif i%3==0:
        print("Fizz")
    elif 1%5==0:
        print("Buzz")
    else:
        print(str(i))
