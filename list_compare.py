l1=[1,2,3,4]
l2=[1,3,4,5,6,7]
print('the 1st list is : ',l1)
print('the 2nd list is : ',l2)

leh1=len(l1)
leh2=len(l2)
if leh1==leh2:
    print("both lists are having same length")
else:
    print("both lists are not having same length")
k=0
for i in range(0, len(l1)):
    k = k + l1[i]
print ("the sum of l1: ",k)
l=0
for j in range(0, len(l2)) :
    l = l + l2[j]
print("the sum of l2: ",l)

if l==k:
    print("the sum of both lists are same")
else :
    print("the sum of both lists are not same")

def common(l1,l2):

    for i in l1:
        for j in l2:
            if i==j:
                print(i)
print("the common elements 2 lists are : ")   
common(l1,l2)