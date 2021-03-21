n=int (input("enter the limit"))
s=0
i=1
while(i<=n):
    s=s+i
    print (s)
    if(s>=25):
        break
    i=i+1
 else:
  print("sum of first ", n," natural numbers is ",s)