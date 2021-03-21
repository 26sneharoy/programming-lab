#9
w=(input("enter your word: "))
length=len(w)
result=w[-1]+w[1:length-1]+w[0]
print(result)