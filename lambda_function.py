l=[1,3,5,6]
print(l)
n=list(map(lambda x: x+2 ,l))#lambda function
print (n)
import functools
l=[1,3,5,6]
print(l)
n=functools.reduce(lambda x,y:x+y,l)#reduce function
print (n)
l=[5,3,12,17,18,24,32]
print (l)
adults=list(filter(lambda x: (x>18),l))#filter function
print (adults)
#letters=['a','b','e','i','o','j']
#print(letters)
#vowel=['a','e','i','o','u']
#vowels=list(filter(lambda x: x==['a','e','i','o','u'],letters))
#print(vowels)
square=lambda x: x*x
a=int(input("side : "))
print("area",square(a))