def fib(num):
    if num <= 1:
        return num
    else:
        return(fib(num-1)+fib(num-2))
    
n=int(input("enter the limit: "))
if n<=0:
    print("enter a positive number")
else:
    print("the fibonnacii series is : ")
    for i in range (n):
        print(fib(i))
