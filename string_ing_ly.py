def add(sent):
    length=len(sent)

    if length>2:
        if sent[-3:]=='ing':

            sent += 'ly'
        else:
        
             sent+=  'ing'

    return sent
sent=input("enter your string : ")
add(sent)
print(add(sent))


   