#8
w=input("enter your word : ")
c=w[0]
w=w.replace(c,"$")
w=c+w[1:]
print("your result is",w)