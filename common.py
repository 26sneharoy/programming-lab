#def common(li1,li2):
   # result=[]
  #  for element in li1:
      #  if element in li2:
        #    result.append(element)
   # return result
#li1=[1,2,3,4]
#li2=[1,3,4,5,6,8]
#print(common(li1,li2))

def common(li1,li2):
    li1=set([1,2,3,4])
    li2=set([1,4,5,6,7])
    if li1 & li2:
        print()
