def fac(n):
    for i in range (1,n+1):
        if n %i==0:
            print(i)
n=int(input("enter the number whose factors to be found : "))
fac(n)