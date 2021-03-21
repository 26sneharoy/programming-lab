square=lambda x: x*x
a=int(input("enter the side : "))
print("area of  square is : ",square(a))

rectangle=lambda a,b: a*b
a=int(input("enter the length : "))
b=int(input("enter the breadth : "))
print("area of rectangle is : ",rectangle(a,b))

triangle =lambda b,h:(1/2)*b*h
b=int(input("enter the base : "))
h=int(input("enter the height : "))
print("area of triangle is : ",triangle(b,h))

