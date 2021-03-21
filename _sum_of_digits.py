def getsum(n):
    strr=str(n)
    list_of_n=list(map(int,strr.strip()))
    return sum(list_of_n)

n=int(input("enter a 2/3 digit number: "))
print(getsum(n))