def palindrome(nw):
    leng=len(nw)
        for i in range (0,len(nw)):
            if nw[0:(len(nw)/2)]==nw[(len(nw)/2)+1:]:
                print("palindrome")
            else:

                print("not palindrome")
nw="radar"
palindrome(nw)

