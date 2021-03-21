def word(new):
    upper=0
    lower=0
    print("length of string is : ",len(new))
    for i in range(0, len(new)):
        if new[i].isupper():
            upper=upper+1
        else:
            lower=lower+1
    print("upper case letters are : ",upper)
    print("lower case letters are : ",lower)
new="animAL"
word(new)