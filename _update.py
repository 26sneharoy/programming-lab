import operator
k ={4:2,3:1,5:6,7:8}
sorted_kdes =dict(sorted(k.items(),key =operator.itemgetter(1),reverse=True))
print('descending order :',sorted_kdes)
sorted_kasc =dict(sorted(k.items(),key =operator.itemgetter(1)))
print("ascending order : ",sorted_kasc)