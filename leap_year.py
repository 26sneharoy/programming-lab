#co 1 2
n=int (input("enter the last year :"))
for i in range (2021,n+1):
   if i%100==0:
      if i%400==0:
          print(i)
   else:
      if i%4==0:
         print(i)

       
    #print('the leap years are ',s)