def longest_word(w):
    word=len(w[0])
    length=w[0]

    for i in w:
        if(len(i)>word):
            word=len(i)
            length=i
    print("the longest word is : ",length)
w=['kamaggumonna','tommy','worsinija']
longest_word(w)