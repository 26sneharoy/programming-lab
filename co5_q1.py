st1="Good Morning""\n""hello everyone""\n""allright""\n"
fw=open("Afile.txt","w")
fw.write(st1)
fw.close()

fr=open("Afile.txt","r")
st2=fr.readlines()
for i in st2:
    print(i)