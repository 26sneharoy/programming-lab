def sum_series(num):
    avn=1
    fact=1
    for i in range(1,num):
        fact *=i
        avn=avn +((2*i+1)/fact)
    return avn
num=int(input("enter the limit : "))
sum_series(num)
print("sum is :",sum_series(num))