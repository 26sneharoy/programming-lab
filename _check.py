s=[1,2,3,5,6,7,8]
n=int(input('enter your number '))
for i in range(len(s)):
   if n==s[i]:
    print('the given number is present')
    break

else:
    print('the given number is not present')