def swapping(a,b):
    a1=b[:1]+a[1:]
    b1=a[:1]+b[1:]
    print("after swapping : ",a1+" "+b1)
swapping('wello' , 'horld')