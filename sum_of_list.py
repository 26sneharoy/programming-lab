import functools
l=[1,2,3,4,5,6,7,8]
print(l)
n=functools.reduce(lambda x,y:x+y,l)#reduce function
print (n)