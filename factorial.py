#to find the factorial co2 1

n=int (input("enter the element :"))
factorial=1
if(n<0):
    print("sorry try non negative number")
elif(n==0):
    print("factorial of  0 is 1")
else:
    for i in range (1,n+1):
        factorial=factorial*i
print("the factorial of",n,"is :",factorial)
