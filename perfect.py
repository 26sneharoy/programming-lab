def perfect(n):
    sum=0
    for i in range(1,n):
        if n%i==0:
            sum=sum+i
    if (sum==n):
        print(n,"is a perfect ")
    else:
        print(n,"is not a perfect number")
n=3
perfect(n)
